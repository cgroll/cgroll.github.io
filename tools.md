---
layout: page
title: Tools
permalink: /tools/
---

"Give me six hours to chop down a tree and I will spend the first four
sharpening the axe." - Abraham Lincoln

<br>

Tools, machines, services: there are many things out there that have
the potential to make our lives easier. But finding the best tools
among the millions of options can be a difficult and time-consuming
process in itself. Hence, I personally find it pretty useful to hear
about the tools and services that other successful people use.
Similarly, I thought it might be helpful for some people if I share my
experiences as well, even though I'm only moderately successful ;-)

<br>

# "Second brain" and organization tools

With increasing age and decreasing brain capacity processing the
constant stream of information that we encounter on a daily basis is
not an easy task. Hence, I rely on a series of tools in order to
steadily take notes, connect the dots between snippets of information
and manage my daily life and tasks. Following are the most important
tools in order to build such a second brain.

### Notion

[Notion.so](https://www.notion.so) is a productivity and organization tool that allows users to
create notes, tasks, wikis, and databases all in one place. It is
often referred to as a "second brain" because it allows users to
centralize and access all of their important information and tasks in
one location. Notion's flexibility and customization options allow
users to tailor it to their specific needs and workflows, making it an
effective tool for staying organized and on top of tasks and projects.

### Instapaper

[Instapaper](https://www.instapaper.com) is a tool for saving and
organizing web pages to a personal library for later viewing, reading
or studying. It minimizes distractions while reading by providing a
customized appearance adjusting the font size, line spacing, and
background color. Additionally, it has a feature called "highlight and
notes" that allows users to highlight specific parts of the article
and add notes to them. These notes can be sync'ed with Notion.so (with
the help of Readwise) and hence are a great way to gradually build up
a personal knowledge database.

### Readwise

[Readwise](https://readwise.io/) is a tool that helps users to review and retain the
information they've read. It works by integrating with popular reading
apps like Kindle, Instapaper and Pocket, and automatically extracts
highlights, notes and annotations that users have made in those apps.
It then presents those notes in a daily email digest, and allows users
to review the information at a scheduled time. By doing so, it helps
users to keep track of what they've read, remember the key points, and
retain the information for longer. However, I mostly use Readwise for
it's ability to sync any notes with Notion.so which is my preferred
tool to stay organized and make the most of the information I've
read by making it easily accessible and reviewable.

### Google cloud services

I generally rely on the set of free cloud-based services from Google.
Gmail is my preferred email service. And Google Keep and Google
Calendar are perfect and lightweight tools for note-taking and
scheduling appointments and reminders, in particular whenever I'm on
the go.

# Software development

## IDE / editor

### Visual Studio Code

Over the years I've tried couple of IDE's and text editors for
software development, note taking and markdown or LaTeX documents. My
current favorite is [Visual Studio
Code](https://code.visualstudio.com/), a highly customizable and
lightweight IDE that is available for Windows, macOS, and Linux
operating systems. It supports a wide range of extensions that can be
installed to enhance its functionality. And it allows customization of
the editor with themes, keyboard shortcuts, and other preferences.
This is a necessary feature for people like me that once climbed the
steep learning curve and used [GNU
Emacs](https://www.gnu.org/software/emacs/) and can't imagine a life
without Emacs shortcuts anymore ;-)

### Emacs

Emacs has a very keyboard-centric interface: it is designed to be used
primarily with the keyboard, which makes it possible to perform many
operations quickly and efficiently. It is also highly customizable and
allows a wide range of text editing capabilities, including syntax
highlighting, auto-completion, search and replace, and recording of
macros. I actually still use it for quick notes, text editing and git
commands through magit.


## Software languages

### Python

At the moment I do most of my coding in
[Python](https://www.python.org/), mostly because I think it has the
best ecosystem for my usecases right now. It comes with great packages
for ML, AI and data science applications. But it also has a great set
of general purpose tools for requirements like unit testing, database
connections, sending / receiving http requests, SDKs for cloud
providers and many more. Also, it is generally well supported by third
party services or frameworks, e.g. AWS lambda functions, Google Earth
Engine, Blender 3D and many more.

### Julia

Before Python I did some for fun coding in
[Julia](https://julialang.org/). I still think that Julia has great
potential because it was designed from the beginning for high
performance. It also comes with a lot of other state of the art syntax
goodies like multiple dispatch, metaprogramming capabilities, abstract
types, multi-threading and many more. I will definitely keep an eye on
Julia, its growing ecosystem and adoption in the industry.


### R

Although Python is my favorite language at the moment,
[R](https://www.r-project.org/) has a great ecosystem of packages as
well, in particular when it comes to statistics and data applications.
It is definitely worthwhile to know at least some of the basics, and I
happen to use R from time to time in order to benefit from some
package that might not yet have a suitable counterpart in the Python
ecosystem.

### Matlab

[Matlab](https://www.mathworks.com/products/matlab.html) was the
language that I used for my first data application (my diploma
thesis), but also was the first language that I used in a production
setup. I still think that it can be a good starting point for
beginners: it comes with a good IDE and a great built-in debugger.
However, due to its proprietary nature Matlab comes with licensing
costs and it also is rather hard to embed into a broader software
infrastructure. It also is rather limited in capabilities for certain
usecases, e.g. data science and AI applications. Most state of the art
research packages are published in open source software languages first.

## Organizing code

### Meld

[Meld](https://gitlab.gnome.org/GNOME/meld) is a visual diff and merge
tool to compare files or directories. It is an open-source software
that runs on Windows, macOS, and Linux operating systems. It provides
users with a graphical user interface that displays the differences
between two or three files side-by-side. This makes it easy to
identify and merge changes made to the code or other text-based files.

### Git

[git](https://git-scm.com/) certainly was a game changer for me when I
started using it roughly a decade ago. I started using it when I had
to sync code between multiple machines (work desktop, laptop at home),
but I soon noticed that it generally forces you to set up a cleaner
folder structure and file history. No more file_v1, file_v2,
file_final labelling required ;-) And of course it reaches its full
potential only when you are working collaboratively with multiple
persons on some project.

### Magit

There are several extensions to git that I use.
[magit](https://magit.vc/) is my favorite entrypoint to quickly
execute git commands with a lot of convenient keyboard shortcuts. But
it requires Emacs, and hence it usually is not the best choice for a
broader audience. But it showed me how much better your git experience
can become when you use some kind of GUI or helpful entrypoint for
git.

### Github desktop, git bash

Whenever I'm working on Windows, I tend to use [Github
Desktop](https://desktop.github.com/) or git bash for more complicated
commands than simple merges and commits.

### MyRepos

I also use [myrepos](https://github.com/RichiH/myrepos) from time to
time when I'm either involved into too many projects and repositories
simultaneously, or when I want to generally make sure that all my
relevant local repositories are up to date. It saves you some time
when you need to fetch all of the latest changes in multiple
repositories.

### git-lfs

For binary and / or large files I mostly use
[git-lfs](https://git-lfs.com/). Although I ran into some
synchronization issues from time to time in projects with multiple
collaborators and files under git-lfs control. So I'm actually still
searching for a better alternative here.

## Reproducible computing and job scheduling

### DVC

One such alternative could be [DVC](https://dvc.org/): data version
control. It has a slightly different way of dealing with large files,
so it is not a perfect substitute. But it is still a great way to keep
track of binary files and / or large files and it actually has an even
much broader scope. It allows you to keep track of which data inputs
and model outputs are associated with each other, so that e.g. in AI
applications you don't lose control of which inputs where used for
which model. But it also allows easy sharing of files amongst multiple
project members so that computationally intensive scripts do not need
to be run multiple times. And if you want, you can also use DVC to
keep track of the sequence of steps and scripts that have to be run in
order to replicate the current project state.


### GNU Make

[GNU Make](https://www.gnu.org/software/make/) was originally invented
as a build automation tool that can be used to automatically build
executable programs and libraries from source code. One needs to
define a set of rules that describe how the various source code files
should be compiled and linked together to produce the final executable
or library. Make uses a file timestamp-based approach to determine
which files need to be rebuilt. This means that if a source file or a
dependency has been modified since the last build, Make will
automatically rebuild the necessary parts of the program. This helps
to ensure that the program is always up-to-date and that unnecessary
rebuilding is avoided.

If you think about it, most projects can actually be defined as a
series of computing steps that need to be followed in a certain
sequence. Once you write down the full series of steps, the project
can be fully reproduced. Or, if you update or change any of the inputs
of the computation sequence, you can compute and update any outputs.
This can be nicely used for machine learning applications, where you
can update your dataset and automatically re-train your model.

### Airflow

While GNU Make can facilitate manually re-running a sequence of
computational steps, you need a more powerful framework if you want to
regularly run scripts (jobs) in a fully automated way. One of the most
popular frameworks to programmatically create, schedule, and monitor
workflows is [Apache Airflow](https://airflow.apache.org/). It was
originally developed by Airbnb and is now an open-source Apache
Software Foundation project. With Airflow, you can define your
workflows as code using Python, which allows you to easily create
complex data pipelines. These pipelines can involve tasks such as
running SQL queries, extracting data from APIs, transforming data, and
loading data into databases or data warehouses. In addition to the
scheduling and computing functionality, Airflow also provides a
web-based user interface for monitoring and managing workflows. This
way you get a nice overview of the status of all jobs in order to
identify any failures and you can see some metrics for your jobs like
average run times. While writing jobs itself is rather trivial, in my
view the hard part with Airflow is setting up an appropriate
infrastructure. You obviously don't want to have Airflow running 24/7
on your laptop, but you need to deploy it to a cloud. So you need to
set up a deploy pipeline, think about how to update your existing
jobs, your Airflow version, your operating system. And depending on
the amount of jobs that you want to run you also need to think about
connecting your Airflow scheduler to a computing cluster that can run
your jobs in parallel.

### Docker

[Docker](https://www.docker.com/) allows you to create snapshots of a
complete software stack, including the application code, runtime,
system tools, and libraries. This is very handy whenever you want to
move your locally developed code to some other machine, e.g. a
computing server or to the cloud. Any code that you run usually comes
with a lot of dependencies and it is a non-trivial task to replicate
the exact codebase on a different machine. E.g. if you want to move
your Python machine learning model to the cloud then first of all you
need to make sure to move the exact version of your code to the cloud.
But besides your own code base, you also need to make sure that you
use the exact same Python packages as well as the same Python
interpreter that you used locally. You can use tools like
[venv](https://docs.python.org/3/library/venv.html) or
[Poetry](https://python-poetry.org/) for this. But in many
applications you also need to fix dependencies that are outside of
your Python stack. For this you would also need to fix certain
libraries of your operating system. E.g. if you want to deploy a model
that does image recognition you might rely on
[OpenCV](https://opencv.org/), or if you work with audio or video
files you might rely on [FFmpeg](https://ffmpeg.org/). So in order to
facilitate re-building an exact computing environment on some other
machine, you can use Docker.


# Computer

As someone who values flexibility, I prefer to work solely on my
laptop without the need for additional screens. This allows me to work
from anywhere with ease. Currently, I use a Lenovo Legion 5 with an
AMD Ryzen 7 6800H processor. The laptop has a large 15.6'' display
with high-resolution, providing me with ample workspace and overview
during coding. Additionally, the laptop boasts a GeForce RTX 3070 GPU,
which I can utilize for computationally intensive tasks such as
machine learning models or 3D graphics rendering. Overall, my setup
allows me to work efficiently and effectively, no matter where I am
for a good price to quality ratio. The only downside is that the
computer only has 16GB RAM and a rather small disk size of 1TB.

### Operation system

Over the years I have found [Ubuntu](https://ubuntu.com/desktop) to be
my favorite operating system. While [Microsoft
Windows](https://www.microsoft.com/en-us/windows?r=1) and its
mouse-click GUI may be the easiest way to get started with computers,
the Linux command line offers a much more efficient way of speeding up
workflows with bash commands and allowing for automation. One of the
major advantages of Ubuntu is that it is free to use, which is why I
have used it in the past when teaching a statistics course in Africa,
where I wanted to ensure all students had access to a free and
reproducible setup. In addition to its cost-effectiveness, Ubuntu also
feels more lightweight than Windows to me. It does not require as many
anti-virus checks and time-consuming updates, making it a more
streamlined and efficient choice for my workflow.

<br>

While Ubuntu is my preferred operating system, I do occasionally use
Windows as well. After all, it is still the standard operating system
used by the majority of computer users. When I want to share
something, it's important to consider the OS used by the people I'm
sharing with (which is most likely Windows). Using the same OS as the
recipient can make the process much smoother. Furthermore, there are
certain programs or drivers that only run on Windows or Mac, so it's
necessary to use those operating systems in those specific cases. For
example, the GPU on my laptop only runs correctly on Windows. In these
situations, I find it necessary to switch to Windows myself to ensure
compatibility and optimal performance. While Ubuntu is my go-to
operating system, it's important to choose the right tool for the job
and sometimes this means using Windows or macOS instead of Ubuntu.


### Password management

[KeepassX](https://www.keepassx.org/) is a free and open-source
password management software that helps users to securely store and
manage their passwords in an encrypted database. It is a
cross-platform application that runs on various operating systems,
including Windows, Linux, and macOS. Using a password manager can
encourage you to use better password practices, such as creating
strong and unique passwords and changing them regularly. Since
passwords are stored in an encrypted database, this means that even if
your computer is hacked or stolen, your passwords cannot be accessed
without the master password.


### Stay sync'ed / back'ed up

[Dropbox](https://www.dropbox.com) is a cloud-based file hosting
service that allows users to store and share files and folders across
multiple devices and with other users. It works by creating a virtual
folder on a user's computer or mobile device. Any file or folder
placed in this folder is automatically uploaded to Dropbox's servers
and synced across all of the user's devices that have Dropbox
installed. This means that users can access their files from anywhere
with an internet connection, whether it's on their computer,
smartphone, or tablet.

<br>

I use Dropbox for several reasons, including syncing my password
database across devices. For example, this allows me to access my
credit card credentials on my mobile phone when I'm on vacation or
away from my computer. Since KeepassX stores any passwords in an
encrypted database, I do not need to worry about data privacy concerns
in the Dropbox cloud. In addition to password syncing, I also use
Dropbox to sync any e-books or PDF articles across devices. This is
particularly useful when I want to read them on my tablet, which has a
bigger screen size and a pen for highlighting. Another key benefit of
using Dropbox is that files or documents are automatically back'ed up
to the server, so you don't have to worry about losses of data when my
device gets stolen or damaged. However, you should think about data
privacy issues before you put all of your data into the cloud.



## MISC


### OBS Studio

[OBS Studio](https://obsproject.com/) (Open Broadcaster Software
Studio) is a free and open-source software for live streaming and
video recording. It currently is my preferred desktop recording
software that I use to create tutorials or other educational videos on
my laptop. It allows users to capture and record video from multiple
sources, including webcams, desktop screens, and applications, and it
is available for Windows, macOS, and Linux operating systems.

### Blender 3D

[Blender 3D](https://www.blender.org/) is one of most impressive
open-source projects that I've ever seen. It offers a comprehensive
suite of tools and features for creating 3D models, textures,
lighting, and animation. Its rendering engine lets you create
photorealistic images and animations, powerful enough that you could
literally use it to create your own Pixar-like animation movie (have a
look at [this](https://youtu.be/XYaw7gf48kQ) YouTube video to see some
awesome examples of Blender 3D outputs). It is just astonishing to see
how powerful free and open-source software can be.
