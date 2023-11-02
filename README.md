<div align="center">

  [<img src="./static/icons/repo_banner.png" alt="SIMPLE AI">](https://github.com/1chooo/simple-ai)<br>
  <em>SIMPLE AI: Bridging the Gap with AI For Everyone</em>

  [![project badge](https://img.shields.io/badge/1chooo-simple__ai-informational)](https://github.com/1chooo/simple-ai)
  [![Made with Python](https://img.shields.io/pypi/pyversions/gradio.svg?color=blue)](https://python.org "Go to Python homepage")
  [![License](https://img.shields.io/badge/License-MIT-blue)](./LICENSE "Go to license section")

[Get Started](#getting-started)
| [Collaboration Guidelines](#collaboration-guidelines)
| [LICENSE](#license)
| [中文](readme_files/zh_cn#readme)

</div>

# SIMPLE AI: Bridging the Gap with AI For Everyone
Hi there 👋🏻 This is **SIMPLE AI**. **SIMPLE AI** is an open-source learning platform  enabling everyone unfamiliar with programming languages to easily engage with AI and open the doors to the world of the future.

## Getting Started
Python version `python3.10.1` with `gradio, scikit-learn, seaborn, pandas, numpy, matplotlib, joblib`

### Build `venv` for **MacOS**
```shell
$ pip3 install virtualenv
$ python3.10 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ deactivate
$ rm -rf venv     # remove the venv
```

### Build `venv` for Windows
```shell
$ pip install virtualenv
$ python3.10 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ deactivate
$ rmdir /s venv     # remove the venv
```
### Build Docs
```shell
$ mkdocs server
$ mkdocs build
```

### Run web app
```shell
$ ./build.sh

# or
$ uvicorn main:app --host 127.0.0.1 --port 5002
```

## Collaboration Guidelines
### Forking this Repository:

Fork the `simple-ai` repository into your own workspace.

### Cloning the Repository to Your Workspace:

```shell
$ git clone git@github.com:<your_workspace_name>/simple-ai.git
```

### Setting Upstream Remote:
```shell=
$ git remote add upstream git@github.com:1chooo/simple-ai.git

$ git remote -v
origin  git@github.com:<your_user_name>/simple-ai.git (fetch)
origin  git@github.com:<your_user_name>/simple-ai.git (push)
upstream        git@github.com:1chooo/simple-ai.git (fetch)
upstream        git@github.com:1chooo/simple-ai.git (push)
```
### Pull Requests:
If you have any valuable ideas to contribute, please create a pull request and provide details about the outstanding work you've done.

### Issue Reporting:
If you encounter any problems while contributing to this project, please report the issues in the [simple-ai/issues](https://github.com/1chooo/simple-ai/issues) section.

### Important Notes:
> [!IMPORTANT]  
> Remember to synchronize and update your repository before starting to write code each time.
> #### Make sure to synchronize and update your repository before initiating a pull request:
> 1. Run `git stash save` to temporarily stash your local changes.
> 2. Run `git fetch upstream` to sync the source project with your local copy.
> 3. Run `git checkout main` to switch to the main branch.
> 4. Run `git merge upstream/main` to merge the updated remote version into your local copy. If there are no conflicts, the update process is complete.
> 5. Run `git stash pop` to apply your temporarily stashed changes back to your working directory. Resolve any conflicts if necessary.


## License
Released under [MIT](./LICENSE) by [Hugo ChunHo Lin](https://github.com/1chooo).

This software can be modified and reused without restriction.
The original license must be included with any copies of this software.
If a significant portion of the source code is used, please provide a link back to this repository.
