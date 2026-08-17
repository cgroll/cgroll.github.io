# /// script
# dependencies = ["playwright"]
# ///
import json
import shutil
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
DECK_HTML = HERE / "deck.html"
OUT_DIR = HERE / "clips"

TIMING_FILE = sys.argv[1] if len(sys.argv) > 1 else "scene_timing.json"
OUT_NAME = sys.argv[2] if len(sys.argv) > 2 else "deck_full.mp4"


def scene_js_data(scene):
    style = scene["visual"]["style"]
    content = scene["visual"].get("content", "")
    lines = content.split("\n") if content else []

    data = {"style": style}
    if style == "checklist":
        data["items"] = lines
    elif style == "cta":
        data["kicker"] = "FULL WRITEUP AND WALKTHROUGH"
        data["content"] = content
    elif style == "teaser":
        data["kicker"] = "COMING UP"
        data["lines"] = lines
    elif style == "pause":
        pass
    else:
        data["lines"] = lines
    if "kicker" in scene["visual"]:
        data["kicker"] = scene["visual"]["kicker"]
    return data


def main():
    data = json.loads((HERE / TIMING_FILE).read_text())
    scenes_by_id = {s["id"]: s for s in data["scenes"]}
    timing = data["timing"]

    video_tmp_dir = OUT_DIR / "_raw_deck"
    if video_tmp_dir.exists():
        shutil.rmtree(video_tmp_dir)
    video_tmp_dir.mkdir(parents=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            record_video_dir=str(video_tmp_dir),
            record_video_size={"width": 1920, "height": 1080},
        )
        page = context.new_page()
        page.goto(f"file://{DECK_HTML}")
        page.wait_for_timeout(300)

        for t in timing:
            scene = scenes_by_id[t["id"]]
            visual = scene["visual"]
            duration_ms = int(max(t["duration"], 0.1) * 1000)

            if visual["kind"] == "text_slide":
                payload = json.dumps(scene_js_data(scene))
                page.evaluate(f"(d) => window.goToSlide(d)", json.loads(payload))
                print(f"scene {t['id']:>2} [{visual['style']:<18}] {duration_ms/1000:.2f}s")
            elif visual["kind"] == "animation_step":
                step = visual["anim_step"]
                group = visual.get("group", "pipeline_speculative")
                fn = {
                    "pipeline_steps": "window.setAnimStep2",
                    "chunk_transcribe": "window.setAnimStep3",
                }.get(group, "window.setAnimStep")
                page.evaluate(f"() => {fn}({step})")
                print(f"scene {t['id']:>2} [{group} step {step:<2}] {duration_ms/1000:.2f}s")
            elif visual["kind"] == "checklist_step":
                args = {"kicker": visual["kicker"], "items": visual["items"], "step": visual["step"]}
                page.evaluate(
                    "(a) => window.setChecklistStep(a.kicker, a.items, a.step)", args
                )
                print(f"scene {t['id']:>2} [{visual['group']} step {visual['step']:<2}] {duration_ms/1000:.2f}s")
            else:
                raise ValueError(visual["kind"])

            page.wait_for_timeout(duration_ms)

        page.wait_for_timeout(200)
        video_path = page.video.path()
        context.close()
        browser.close()

    final_clip = OUT_DIR / OUT_NAME
    shutil.copy(video_path, final_clip)
    shutil.rmtree(video_tmp_dir)
    print(f"\nWrote {final_clip}")


if __name__ == "__main__":
    main()
