---
layout: post
title:  "Async Python"
date:   2025-06-02
categories: [Tools]
excerpt: > #
  Understanding When Your Code *Actually* Pauses.
math: false
---

Ever written a program that needs to fetch data from a couple of websites or read a few files? If you do it sequentially, your program spends a lot of time just waiting around. Asynchronous programming with Python's `asyncio` helps solve this, allowing your program to manage multiple I/O-bound operations concurrently, making it much more efficient.

But a common point of confusion is understanding exactly when your asynchronous function yields control, allowing other operations to run. Let's dive into a tiny example to make this crystal clear.

### The Key Idea: `await` is the Yield Point

In `asyncio`, an `async def` function (a coroutine) can be "paused" using the `await` keyword. When your coroutine `await`s something (like an I/O operation or another coroutine), it tells the asyncio event loop, "I'm going to be waiting for a bit; feel free to run something else in the meantime."

Crucially, any code *before* the first `await` in your coroutine runs synchronously as part of that coroutine's execution turn.

### A Simple Python Example

Let's look at a minimal piece of code. We have a `main` coroutine that schedules two "fetch" tasks. `Task A` is a bit longer than `Task B`.

```python
import asyncio

async def fetch_url(url_name, delay):
    """Simulates a network request by pausing."""
    # In a real app, this is where you'd await an actual I/O call,
    # e.g., await client.get(url)
    await asyncio.sleep(delay)
    return f"Data from {url_name}"

async def main():
    """Main coroutine to demonstrate task scheduling and awaiting."""
    # 1. Schedule Task A (long operation)
    task_a = asyncio.create_task(fetch_url("A (long)", 3))
    # 2. Schedule Task B (short operation)
    task_b = asyncio.create_task(fetch_url("B (short)", 1))

    # 3. CRITICAL POINT: This line executes as part of main()'s synchronous flow,
    #    *after* tasks are scheduled but *before* main() itself awaits and yields control.
    print("[Main]: Tasks A & B scheduled. My own synchronous code continues UNTIL the first 'await'.")

    # 4. Main encounters its first 'await', pauses, and yields control to the event loop.
    #    The event loop can now run the scheduled tasks (Task A and Task B).
    result_a = await task_a

    # 7. Main resumes after task_a completes. It then encounters 'await task_b'.
    #    If task_b is already complete, this resolves quickly.
    result_b = await task_b

    return f"Final: {result_a}, {result_b}"

# To run this example (e.g., in a .py file):
# if __name__ == "__main__":
#     final_output = asyncio.run(main())
#     # The print below is just to see the output if you run the file.
#     # The core logic is demonstrated by the print statement within main().
#     print(f"Output from main: {final_output}")
```

The most important line here is the `print` statement *after* `asyncio.create_task` calls but *before* the first `await result_a`. This shows that `main()` doesn't immediately cede control when tasks are created.

### Control Flow Breakdown

Here’s the sequence of events in our example's core logic:

1.  **`task_a = asyncio.create_task(fetch_url("A (long)", 3))`**:
    * The `fetch_url("A (long)", 3)` coroutine is wrapped in `Task A` and scheduled on the event loop. `main()` continues immediately.
2.  **`task_b = asyncio.create_task(fetch_url("B (short)", 1))`**:
    * The `fetch_url("B (short)", 1)` coroutine is wrapped in `Task B` and scheduled on the event loop. `main()` continues immediately.
3.  **`print("[Main]: Tasks A & B scheduled. My own synchronous code continues UNTIL the first 'await'.")`**:
    * This line is executed synchronously by `main()`. It confirms `main()` is still running its own code after scheduling tasks but before it has yielded control via an `await`.
4.  **`result_a = await task_a`**:
    * `main()` encounters its first `await`, targeting `Task A`.
    * `main()` **suspends** its execution here. Control is yielded to the asyncio event loop.
    * The event loop runs the scheduled tasks:
        * It starts `Task A`. `Task A` executes `fetch_url(...)` until `await asyncio.sleep(3)`, then `Task A` suspends.
        * The event loop then starts `Task B`. `Task B` executes `fetch_url(...)` until `await asyncio.sleep(1)`, then `Task B` suspends.
    * Both tasks are now "sleeping" concurrently. `Task B` (1s sleep) finishes its sleep before `Task A` (3s sleep).
    * Once `Task A` fully completes (after its 3s sleep), `main()` will resume from this `await task_a` line, and `result_a` gets its value.
5.  **`result_b = await task_b`**:
    * `main()`, now resumed, encounters its second `await`, targeting `Task B`.
    * Since `Task B` (1s sleep) already completed while `main()` was waiting for `Task A`, this `await task_b` resolves immediately. `result_b` gets its value. `main()` doesn't suspend for any significant time here.
    * `main()` then proceeds to finish.

A sequence diagram can help visualize this yielding and resuming of control:

![Sequence diagram](/assets/images/async_python.png)

### Key Takeaway

The power of `asyncio` comes from this cooperative yielding. Your coroutines run their synchronous parts and then explicitly `await` when they need to wait for something, allowing the event loop to efficiently manage other tasks. Understanding that your code *after* `asyncio.create_task` but *before* the first `await` in that same coroutine still runs synchronously is key to correctly structuring your async programs.

**Disclaimer**: This post is the result of me chatting with an AI to dust off my knowledge on this topic. The AI then kindly drafted this summary based on our talk and my outline, serving as my personal ‘don’t forget!’ note for the future – because apparently, my brain isn’t a perfect recording device. I’ve made minor edits for clarity.