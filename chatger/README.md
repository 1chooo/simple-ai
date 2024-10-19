# Chatter Judge

Chatter Judge is a FastAPI-based module designed by @1chooo (Hugo ChunHo Lin) to provide a simple judging platform integrated with ChatGPT. This module allows users to interact with the ChatGPT model through a web interface, making it easy to submit queries and receive responses.

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
> [!IMPORTANT]  
> #### Make sure to synchronize and update your repository before initiating a pull request:
> 1. Run `git stash save` to temporarily stash your local changes.
> 2. Run `git fetch upstream` to sync the source project with your local copy.
> 3. Run `git checkout main` to switch to the main branch.
> 4. Run `git merge upstream/main` to merge the updated remote version into your local copy. If there are no conflicts, the update process is complete.
> 5. Run `git stash pop` to apply your temporarily stashed changes back to your working directory. Resolve any conflicts if necessary.

## Build and run with docker
# 重要
# please download token.json and put in at web\token.json
```shell
$ cp .env.example .env
# now edit the .env file to set the GEMINI_API_KEY, then:
# build the docker image and run the container
$ docker-compose up -d
# follow the logs
$ docker-compose logs -f
# stop the container but keep the container
$ docker-compose stop
# stop the container and discard the container
$ docker-compose down
```
<!-- 王子祐的註解:帳號密碼需註冊，無寫死
wsl unexpected error 請刪除windows sys
docker run -d -p 80:80 docker/getting-started
如果依賴項變更請使用 c 替換 
-->
### Build Docs
```shell
$ mkdocs server
$ mkdocs build
```

### Format and Lint

```shell
# format the code
$ ruff format .
# check the code
$ ruff check .
# apply the autofix
$ ruff check --fix .
```

## License
Released under [MIT](./LICENSE) by [Hugo ChunHo Lin](https://github.com/1chooo).

This software can be modified and reused without restriction.
The original license must be included with any copies of this software.
If a significant portion of the source code is used, please provide a link back to this repository.

## gemini api method 
```shell
# api key for gemini 1.0 pro(chatbot)
# token.json for code advice from finetune model
```

