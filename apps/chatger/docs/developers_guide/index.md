# Welcome Contributors

大家好，

我們很高興向大家介紹這個開源專案的撰寫風格。我們期望您能與我們一同參與，完成這次的專案。同時，我們將在這裡詳細記錄我們在開發過程中遇到的問題以及我們提出的解決方案。我們希望這能對大家有所幫助。

期待您的參與！

Hello everyone,

We are excited to present the writing style for this open-source project. We hope that you can join us in completing this project together. Additionally, we will document the challenges we encounter during development and the solutions we propose right here. Our aim is to provide assistance and insights for everyone involved.

Looking forward to your participation!

## Collaboration Guidelines
### Forking this Repository:

Fork the [`chatter-judge`](https://github.com/1chooo/chatter-judge) repository into your own workspace.

### Cloning the Repository to Your Workspace:

```shell
$ git clone git@github.com:<your_workspace_name>/chatter-judge.git
```

### Setting Upstream Remote:
```shell
$ git remote add upstream git@github.com:1chooo/chatter-judge.git

$ git remote -v
origin  git@github.com:<your_user_name>/chatter-judge.git (fetch)
origin  git@github.com:<your_user_name>/chatter-judge.git (push)
upstream        git@github.com:1chooo/chatter-judge.git (fetch)
upstream        git@github.com:1chooo/chatter-judge.git (push)
```
### Pull Requests:
If you have any valuable ideas to contribute, please create a pull request and provide details about the outstanding work you've done.

### Issue Reporting:
If you encounter any problems while contributing to this project, please report the issues in the [chatter-judge/issues](https://github.com/1chooo/chatter-judge/issues) section.

### Important Notes:

#### Make sure to synchronize and update your repository before initiating a pull request:

1. Run `git stash save` to temporarily stash your local changes.
2. Run `git fetch upstream` to sync the source project with your local copy.
3. Run `git checkout main` to switch to the main branch.
4. Run `git merge upstream/main` to merge the updated remote version into your local copy. If there are no conflicts, the update process is complete.
5. Run `git stash pop` to apply your temporarily stashed changes back to your working directory. Resolve any conflicts if necessary.

## Developing Requirements

Python version `python3.10` or later.

### Build `venv` for **MacOS**
```shell
$ python3.10 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ deactivate
$ rm -rf venv     # remove the venv
```

### Build `venv` for **Windows**
```shell
$ pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ deactivate
$ rmdir /s venv     # remove the venv
```

### Run web app
```shell
$ ./build.sh

# or
$ uvicorn run:main --host 127.0.0.1 --port 5002
```

### Build Docs
```shell
$ mkdocs server
$ mkdocs build
```

## Project Structure
```shell
PROJECT_ROOT
├── .github/
├── Chatter/
├── docs/
├── static/
├── test/
├── .gitignore
├── build.sh
├── CODE_OF_CONDUCT.md
├── LICENSE
├── mkdocs.yml
├── README.md
├── requirements.txt
└── run.py
```
