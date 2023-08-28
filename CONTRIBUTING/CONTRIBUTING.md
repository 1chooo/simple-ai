# Contributing to AI For Beginner

We want to make contributing to this project as easy and transparent as possible.

## Forking this Repository:

Fork the `simple-ai` repository into your own workspace.

## Cloning the Repository to Your Workspace:

```shell
$ git clone git@github.com:<your_workspace_name>/simple-ai.git
```

## Setting Upstream Remote:
```shell=
$ git remote add upstream git@github.com:1chooo/simple-ai.git

$ git remote -v
origin  git@github.com:<your_user_name>/simple-ai.git (fetch)
origin  git@github.com:<your_user_name>/simple-ai.git (push)
upstream        git@github.com:1chooo/simple-ai.git (fetch)
upstream        git@github.com:1chooo/simple-ai.git (push)
```
## Pull Requests:
If you have any valuable ideas to contribute, please create a pull request and provide details about the outstanding work you've done.

## Issue Reporting:
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
