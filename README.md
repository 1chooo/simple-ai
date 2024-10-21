<a href="https://1chooo.com">
  <img alt="Refinaid Source Code" src="./.github/banner.png">
</a>

<p align="center">
  <img alt="" src="https://img.shields.io/badge/1chooo-refinaid-informational?style=for-the-badge&labelColor=000">
  <img alt="" src="https://img.shields.io/pypi/pyversions/gradio.svg?style=for-the-badge&labelColor=000">
  <img alt="" src="https://img.shields.io/github/license/1chooo/refinaid?style=for-the-badge&labelColor=000">
  <img src="https://img.shields.io/github/stars/1chooo/refinaid?style=for-the-badge&labelColor=000" alt="Novel.sh's GitHub repo">
</p>


# Refinaid: Bridging the Gap with AI For Everyone
Hi there 👋🏻 This is **Refinaid**. **Refinaid** is an open-source learning platform enabling everyone unfamiliar with programming languages to easily engage with AI and open the doors to the world of the future.

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

Fork the `refinaid` repository into your own workspace.

### Cloning the Repository to Your Workspace:

```shell
$ git clone git@github.com:<your_workspace_name>/refinaid.git
```

### Setting Upstream Remote:
```shell
$ git remote add upstream git@github.com:1chooo/refinaid.git

$ git remote -v
origin  git@github.com:<your_user_name>/refinaid.git (fetch)
origin  git@github.com:<your_user_name>/refinaid.git (push)
upstream        git@github.com:1chooo/refinaid.git (fetch)
upstream        git@github.com:1chooo/refinaid.git (push)
```
### Pull Requests:
If you have any valuable ideas to contribute, please create a pull request and provide details about the outstanding work you've done.

### Issue Reporting:
If you encounter any problems while contributing to this project, please report the issues in the [refinaid/issues](https://github.com/1chooo/refinaid/issues) section.

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
Released under [Apache-2.0 license](./LICENSE) by [Hugo ChunHo Lin](https://github.com/1chooo).

This software can be modified and reused without restriction.
The original license must be included with any copies of this software.
If a significant portion of the source code is used, please provide a link back to this repository.
