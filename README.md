# Simple AI - Bridging the Gap with AI For Everyone

[![project badge](https://img.shields.io/badge/1chooo-simple__ai-informational)](https://github.com/1chooo/simple-ai)
[![Made with Python](https://img.shields.io/badge/Python=3.10.1-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
[![License](https://img.shields.io/badge/License-MIT-blue)](./LICENSE "Go to license section")

Enabling everyone unfamiliar with programming languages to easily engage with AI and open the doors to the world of the future.

## Getting Started
Python version `python3.10.1` with `gradio, scikit-learn, seaborn, pandas, numpy, matplotlib, joblib`

### Build `venv` for **MacOS**
```shell
$ pip3 install virtualenv
$ virtualenv venv --python=python3.10.1
$ source venv/bin/activate
$ pip install -r requirements.txt
$ deactivate
$ rm -rf venv     # remove the venv
```

### Build `venv` for Windows
```shell
$ pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ deactivate
$ rmdir /s venv     # remove the venv
```
### Build Docs
```shell
$ pip install mkdocs
$ pip install mkdocs-material
$ pip install pymdown-extensions
$ pip install mkdocstrings
$ pip install mkdocs-git-revision-date-plugin
$ pip install mkdocs-jupyter
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

## Refinaid Team
<table>
  <tr>
    <td align="center"><a href="https://1chooo-github-io.vercel.app/"><img src="https://avatars.githubusercontent.com/u/94162591?v=4" width="100px;" alt=""/><br /><sub><b>1chooo</b></sub></a><br /><a href="https://github.com/1chooo/simple-ai/commits?author=1chooo" title="Code">💻 🧳</a></td>
    <td align="center"><a href="https://github.com/ReeveWu"><img src="https://avatars.githubusercontent.com/u/110542858?v=4" width="100px;" alt=""/><br /><sub><b>ReeveWu</b></sub></a><br /><a href="https://github.com/1chooo/simple-ai/commits?author=ReeveWu" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/VincentLi1216"><img src="https://avatars.githubusercontent.com/u/98581766?v=4" width="100px;" alt=""/><br /><sub><b>VincentLi1216</b></sub></a><br /><a href="https://github.com/1chooo/simple-ai/commits?author=VincentLi1216" title="Code">💻</a></td>
  </tr>
</table>
