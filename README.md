# A Basic Python Project Template

## Version 1.0.0

_**A logical, reasonably standardized, but flexible project structure for doing and sharing data science work.**_

## Why use a standardized project template?
### *(Text below liberally copied from https://drivendata.github.io/cookiecutter-data-science/, with light modification. Credit for the below belongs to the [drivendata team](http://www.drivendata.org/).)*

> it's best to start with a clean, logical structure and stick to it throughout the _entire_ process, from exploratory analysis through to production application.

When we think about data analysis, we often think just about the resulting reports, insights, or visualizations. While these end products are generally the main event, it's easy to focus on making the products look nice and ignore the quality of the code that generates them. Because these end products are created programmatically, **code quality is still important!** And we're not talking about bikeshedding the indentation aesthetics or pedantic formatting standards — ultimately, data science code quality is about correctness and reproducibility.

It's no secret that good analyses are often the result of very scattershot and serendipitous explorations. Tentative experiments and rapidly testing approaches that might not work out are all part of the process for getting to the good stuff, and there is no magic bullet to turn data exploration into a simple, linear progression.

That being said, once started it is not a process that lends itself to thinking carefully about the structure of your code or project layout, so it's best to start with a clean, logical structure and stick to it throughout the _entire_ process, from exploratory analysis through to production application. It's a pretty big win all around to use a fairly standardized setup like this one. Here's why:

#### Other people will thank you

A well-defined, standard project structure means that a newcomer can begin to understand an analysis without digging in to extensive documentation. It also means that they don't necessarily have to read 100% of the code before knowing where to look for very specific things.

Well organized code tends to be self-documenting in that the organization itself provides context for your code without much overhead. People will thank you for this because they can:

* Collaborate more easily with you on this analysis
* Learn from your analysis about the process and the domain
* Feel confident in the conclusions at which the analysis arrives

A good example of this can be found in any of the major web development frameworks like Django or Ruby on Rails. Nobody sits around before creating a new Rails project to figure out where they want to put their views; they just run `rails new` to get a standard project skeleton like everybody else. Because that default project structure is logical and reasonably standard across most projects, it is much easier for somebody who has never seen a particular project to figure out where they would find the various moving parts.

Another great example is the [Filesystem Hierarchy Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard) for Unix-like systems. The /etc directory has a very specific purpose, as does the `/tmp` folder, and everybody (more or less) agrees to honor that social contract. That means a Red Hat user and an Ubuntu user both know roughly where to look for certain types of files, even when using each other's system — or any other standards-compliant system for that matter!

Ideally, that's how it should be when a colleague opens up your data science project.

#### You will thank you
Ever tried to reproduce an analysis that you did a few years ago or even a few _months_ ago? You may have written the code, but it's now impossible to decipher whether you should use `make_figures.py.old`, `make_figures_working.py` or `new_make_figures01.py` to get things done. Here are some questions we've learned to ask with a sense of existential dread:

* Are we supposed to go in and join the column X to the data before we get started or did that come from one of the notebooks?
* Come to think of it, which notebook do we have to run first before running the plotting code: was it "process data" or "clean data"?
* Where did the shapefiles get downloaded from for the geographic plots?
* Et cetera, times infinity.

These types of questions are painful and are symptoms of a disorganized project. A good project structure encourages practices that make it easier to come back to old work, for example separation of concerns, abstracting analysis as a [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph), and engineering best practices like version control.

#### Set yourself up for the future
What happens when that exploratory analysis you're working on morphs from a simple report-and-recommend to a predictive model halfway through a project's lifecycle?  Using a kitchen-sink-included template like this enables you to quickly pivot and deliver a docker image containing your trained model with a minimum of overhead.

#### Nothing here is binding
> "A foolish consistency is the hobgoblin of little minds" — Ralph Waldo Emerson (and [PEP 8](https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds)!)

Disagree with a couple of the default folder names? Working on a project that's a little nonstandard and doesn't exactly fit with the current structure? Prefer to use a different package than one of the (few) defaults?

**_Go for it!_** This is a lightweight structure, and is intended to be a good starting point for many projects. Or, as PEP 8 put it:

> Consistency within a project is more important. Consistency within one module or function is the most important. ... However, know when to be inconsistent -- sometimes style guide recommendations just aren't applicable. When in doubt, use your best judgment. Look at other examples and decide what looks best. And don't hesitate to ask!

# Usage

The project template is structured as follows:
```
.
├── .bumpversion.cfg
├── .dockerignore
├── .gitignore
├── Dockerfile
├── Makefile
├── analysis
│   ├── data
│   ├── notebooks
│   │   └── 0-initial-exploration.ipynb
│   ├── references
│   └── reports
│       └── figures
├── app
│   └── run.py
├── docs
├── models
├── requirements.txt
├── setup.cfg
├── setup.py
├── src
│   └── {{cookiecutter.package_name}}
│       ├── __init__.py
│       ├── etl.py
│       ├── predict.py
│       └── train.py
└── tests
    ├── test_edge_cases.py
    ├── test_exception_handling.py
    ├── test_performance.py
    ├── test_schema.py
    └── test_{{cookiecutter.package_name}}.py
```

To create a new project from this template,

1. Make sure you have cookiecutter installed on your machine (already available on Domino):
    - `sudo apt install cookiecutter` or `conda install cookiecutter` or `pip install cookiecutter`
1. Call cookiecutter to fill out the project structure for your new project:
    - `cookiecutter git+http://github.com/hummel/python-minimal-cookiecutter.git `

Cookiecutter will then prompt you to provide the following values:

* A human-readable Project Name
    - **NOTE**: the name you give your project will be used throughout the codebase, so give it some thought.
* Name of the project owner
* Email address for the project owner
* Brief (one sentence) description of the project
* Package name (defaults to standardized version of project name)
* Git repository URL
* Package repository URL (git repo url + package name)
* Docker base image
* Docker image name

Once you've provided those, cookiecutter will go through and create a directory called `project_name` and fill it in with the files from the template, replacing all entries enclosed in `{{ }}` with the corresponding value you provided.

Finally,

1. Create a new git repository to house your project. Make the repository name match that of the project `name` from `setup.cfg` (same as the 'package_name' you used filling out the template, but with dashes rather than underscores); also add the same brief description of the project.
1. DO NOT initialize the project with a README.
1. Clone the newly-created project repo to your machine, and follow the on-screen instructions to initialize your project as a git repository and push your files to Github.
