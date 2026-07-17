# Complete Git & GitHub Guide

---

## Table of Contents

1. [What is Git?](#1-what-is-git)
2. [What is GitHub?](#2-what-is-github)
3. [Installing Git](#3-installing-git)
4. [Git Configuration](#4-git-configuration)
5. [Key Concepts & Terminology](#5-key-concepts--terminology)
6. [Git Workflow](#6-git-workflow)
7. [Repository](#7-repository)
8. [Staging Area](#8-staging-area)
9. [Commits](#9-commits)
10. [Branches](#10-branches)
11. [Merging](#11-merging)
12. [Merge Conflicts](#12-merge-conflicts)
13. [Remote Repositories](#13-remote-repositories)
14. [Push & Pull](#14-push--pull)
15. [Cloning](#15-cloning)
16. [Forking](#16-forking)
17. [Pull Requests (PR)](#17-pull-requests-pr)
18. [Git Fetch vs Git Pull](#18-git-fetch-vs-git-pull)
19. [Git Stash](#19-git-stash)
20. [Git Log & History](#20-git-log--history)
21. [Git Diff](#21-git-diff)
22. [Undoing Changes](#22-undoing-changes)
23. [Git Reset](#23-git-reset)
24. [Git Revert](#24-git-revert)
25. [Git Rebase](#25-git-rebase)
26. [Git Cherry Pick](#26-git-cherry-pick)
27. [Git Tags](#27-git-tags)
28. [Git Ignore](#28-git-ignore)
29. [Git Aliases](#29-git-aliases)
30. [Branch Protection Rules](#30-branch-protection-rules)
31. [GitHub Actions (CI/CD)](#31-github-actions-cicd)
32. [GitHub Issues](#32-github-issues)
33. [GitHub Projects](#33-github-projects)
34. [GitHub Collaborators](#34-github-collaborators)
35. [GitHub Organizations](#35-github-organizations)
36. [SSH vs HTTPS](#36-ssh-vs-https)
37. [Git Workflow Strategies](#37-git-workflow-strategies)
38. [Common Git Commands Cheat Sheet](#38-common-git-commands-cheat-sheet)

---

## 1. What is Git?

Git is a **version control system (VCS)**. It tracks every change you make to your files so you can:
- Go back to any previous version
- See who changed what and when
- Work with multiple people without overwriting each other's work

Git works **locally on your computer** — you don't need internet to use it.

---

## 2. What is GitHub?

GitHub is a **cloud platform** that hosts your Git repositories online so that:
- Your code is backed up
- Others can see, clone, or contribute to your code
- Teams can collaborate using Pull Requests, Issues, and Reviews

> Think of Git as the engine and GitHub as the garage where you park and share your car.

---

## 3. Installing Git

**Windows:**
Download from https://git-scm.com and run the installer.

**Check if Git is installed:**
```bash
git --version
```

---

## 4. Git Configuration

Before using Git, tell it who you are. This info is attached to every commit you make.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

**View your config:**
```bash
git config --list
```

---

## 5. Key Concepts & Terminology

| Term | Meaning |
|------|---------|
| **Repository (Repo)** | A folder tracked by Git |
| **Commit** | A saved snapshot of your changes |
| **Branch** | A separate line of development |
| **Merge** | Combining one branch into another |
| **Remote** | The online version of your repo (e.g. GitHub) |
| **Clone** | Copying a remote repo to your local machine |
| **Fork** | Your own copy of someone else's repo on GitHub |
| **Pull Request (PR)** | A request to merge your branch into another |
| **HEAD** | Pointer to the current commit you are on |
| **Origin** | Default name for the remote repo |

---

## 6. Git Workflow

The basic day-to-day Git workflow:

```
Make changes → Stage changes → Commit → Push to GitHub
```

```bash
git add .                        # stage changes
git commit -m "your message"     # save snapshot
git push origin branch-name      # upload to GitHub
```

---

## 7. Repository

A repository is a project folder that Git is tracking.

**Create a new repo locally:**
```bash
git init
```
This creates a hidden `.git` folder inside your project — that's where Git stores all history.

**Create a repo on GitHub:**
Go to GitHub → New Repository → Fill in name → Create

---

## 8. Staging Area

The staging area is like a **draft box** before you commit. You choose exactly which changes to include in your next commit.

```bash
git add filename.txt       # stage one file
git add .                  # stage all changes
git status                 # see what is staged and what is not
```

---

## 9. Commits

A commit is a **permanent snapshot** of your staged changes.

```bash
git commit -m "feat: add login page"
```

**Good commit message rules:**
- Be short and clear
- Use present tense ("add" not "added")
- Common prefixes:
  - `feat:` — new feature
  - `fix:` — bug fix
  - `docs:` — documentation change
  - `refactor:` — code cleanup
  - `chore:` — maintenance tasks

---

## 10. Branches

A branch is an **independent line of development**. The default branch is usually called `main`.

```bash
git branch                        # list all branches
git branch feature/login          # create new branch
git checkout feature/login        # switch to branch
git checkout -b feature/login     # create AND switch in one command
git branch -d feature/login       # delete branch (after merging)
```

**Why use branches?**
- Work on a feature without breaking the main code
- Multiple people can work on different features at the same time

---

## 11. Merging

Merging brings changes from one branch into another.

```bash
git checkout dev                  # go to the branch you want to merge INTO
git merge feature/login           # merge feature branch into dev
```

**Types of merges:**

| Type | When it happens |
|------|----------------|
| **Fast-forward** | No new commits on target branch — just moves pointer forward |
| **3-way merge** | Both branches have new commits — Git creates a merge commit |

---

## 12. Merge Conflicts

A conflict happens when two people edit the **same line** in the same file differently and Git cannot decide which version to keep.

**Git will mark the conflict in the file like this:**
```
<<<<<<< HEAD
your version of the line
=======
your friend's version of the line
>>>>>>> feature/login
```

**How to resolve:**
1. Open the file
2. Decide which version to keep (or combine both)
3. Delete the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
4. Stage and commit the resolved file

```bash
git add filename.txt
git commit -m "fix: resolve merge conflict"
```

---

## 13. Remote Repositories

A remote is a version of your repo hosted online (GitHub).

```bash
git remote -v                                  # view remotes
git remote add origin https://github.com/...  # link local repo to GitHub
git remote remove origin                       # remove remote
```

---

## 14. Push & Pull

**Push** — send your local commits to GitHub:
```bash
git push origin branch-name
git push -u origin branch-name    # -u sets upstream (only needed first time)
```

**Pull** — get latest changes from GitHub to your local machine:
```bash
git pull origin branch-name
```

---

## 15. Cloning

Cloning copies an entire remote repo to your local machine.

```bash
git clone https://github.com/username/repo-name.git
```

This creates a folder with all files and the full Git history.

---

## 16. Forking

Forking creates **your own copy of someone else's repo** on GitHub.

- Used when you don't have write access to the original repo
- You make changes in your fork and then open a PR to the original repo
- Common in open source contributions

**Fork vs Clone:**
| | Fork | Clone |
|-|------|-------|
| Where | On GitHub (your account) | On your local machine |
| Used for | Contributing to others' repos | Working on any repo locally |

---

## 17. Pull Requests (PR)

A Pull Request is a **request to merge your branch into another branch** on GitHub.

**Steps to open a PR:**
1. Push your feature branch to GitHub
2. Go to the repo on GitHub
3. Click **Pull requests** → **New pull request**
4. Set **base** (where you want to merge INTO) and **compare** (your branch)
5. Add title and description
6. Submit — collaborators review and approve
7. Merge the PR

**PR is the core of team collaboration** — it allows code review before anything lands on important branches.

---

## 18. Git Fetch vs Git Pull

Both get updates from GitHub but behave differently:

| Command | What it does |
|---------|-------------|
| `git fetch` | Downloads changes but does NOT apply them to your code |
| `git pull` | Downloads changes AND immediately merges them into your current branch |

```bash
git fetch origin          # safe — just checks what changed
git pull origin dev       # fetches + merges in one step
```

Use `fetch` when you want to see what changed before merging. Use `pull` when you're ready to update your local branch.

---

## 19. Git Stash

Stash temporarily **saves your uncommitted changes** so you can switch branches without losing work.

```bash
git stash                  # save current changes
git stash list             # see all stashes
git stash pop              # bring back the latest stash
git stash drop             # delete the latest stash
git stash clear            # delete all stashes
```

**Example use case:**
You are working on a feature but need to urgently fix a bug on another branch. Stash your work, fix the bug, then pop the stash and continue.

---

## 20. Git Log & History

View the commit history of your repo:

```bash
git log                          # full history
git log --oneline                # one line per commit (cleaner)
git log --oneline --graph        # visual branch graph
git log --author="Your Name"     # filter by author
git log filename.txt             # history of a specific file
```

---

## 21. Git Diff

See exactly what changed in your files:

```bash
git diff                         # unstaged changes
git diff --staged                # staged changes (ready to commit)
git diff branch1 branch2         # difference between two branches
git diff commit1 commit2         # difference between two commits
```

---

## 22. Undoing Changes

**Undo changes in a file before staging:**
```bash
git checkout -- filename.txt     # restore file to last commit state
```

**Unstage a file (keep changes but remove from staging):**
```bash
git restore --staged filename.txt
```

**Undo last commit but keep changes:**
```bash
git reset --soft HEAD~1
```

---

## 23. Git Reset

Reset moves your branch pointer back to a previous commit.

```bash
git reset --soft HEAD~1    # undo commit, keep changes staged
git reset --mixed HEAD~1   # undo commit, keep changes unstaged (default)
git reset --hard HEAD~1    # undo commit, DELETE all changes permanently
```

> Be careful with `--hard` — changes are gone forever.

---

## 24. Git Revert

Revert creates a **new commit that undoes a previous commit** — safe to use on shared branches.

```bash
git revert <commit-hash>
```

Unlike `reset`, revert does not rewrite history. Always use `revert` on `main`, `staging`, or `dev` — never `reset`.

---

## 25. Git Rebase

Rebase moves your branch commits on top of another branch — keeps history clean and linear.

```bash
git checkout feature/login
git rebase dev               # put feature commits on top of dev
```

**Rebase vs Merge:**
| | Merge | Rebase |
|-|-------|--------|
| History | Keeps all history with a merge commit | Linear, cleaner history |
| Safe for shared branches? | Yes | No — never rebase public branches |

---

## 26. Git Cherry Pick

Cherry pick applies a **specific commit** from one branch onto another.

```bash
git cherry-pick <commit-hash>
```

**Use case:** You made a bug fix on a feature branch and want to apply just that fix to `main` without merging the entire branch.

---

## 27. Git Tags

Tags mark a specific commit — usually used for **version releases**.

```bash
git tag v1.0.0                          # create a tag
git tag -a v1.0.0 -m "First release"   # annotated tag with message
git push origin v1.0.0                  # push tag to GitHub
git tag                                  # list all tags
git tag -d v1.0.0                       # delete a tag
```

---

## 28. Git Ignore

`.gitignore` tells Git to **ignore certain files** — they will never be tracked or committed.

**Create a `.gitignore` file in your repo root:**
```
node_modules/
.env
*.log
dist/
.DS_Store
```

Common things to ignore:
- `node_modules/` — dependencies (can be reinstalled)
- `.env` — secret keys and passwords
- `*.log` — log files
- `dist/` or `build/` — compiled output

---

## 29. Git Aliases

Aliases let you create shortcuts for long Git commands.

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.lg "log --oneline --graph"
```

Now instead of `git status` you can type `git st`.

---

## 30. Branch Protection Rules

Branch protection prevents direct pushes to important branches and enforces a PR workflow.

**Common rules:**
- Require pull request before merging
- Require at least 1 approval
- Dismiss stale reviews on new commits
- Block force pushes
- Block branch deletion
- Apply rules to admins too

Set up in GitHub → Repo → Settings → Branches → Add rule.

---

## 31. GitHub Actions (CI/CD)

GitHub Actions automates tasks like running tests, checking code, or deploying — every time you push or open a PR.

**Example — run tests on every push:**
```yaml
# .github/workflows/test.yml
name: Run Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm install
      - run: npm test
```

This file goes in `.github/workflows/` in your repo.

---

## 32. GitHub Issues

Issues are used to **track bugs, tasks, and feature requests**.

- Go to repo → Issues → New Issue
- Add a title, description, labels, and assignee
- Reference an issue in a commit: `git commit -m "fix: login bug closes #5"`
- Writing `closes #5` in a PR description automatically closes issue #5 when merged

---

## 33. GitHub Projects

GitHub Projects is a **kanban board** to manage your issues and tasks visually.

- Create columns like: `To Do`, `In Progress`, `Done`
- Drag issues/PRs between columns
- Good for tracking sprint work as a team

---

## 34. GitHub Collaborators

Collaborators are people you invite to have access to your private or public repo.

**Permission levels:**
| Role | Can do |
|------|--------|
| Read | View and clone |
| Triage | Manage issues and PRs (no code push) |
| Write | Push code, merge PRs |
| Maintain | Manage repo settings (no admin) |
| Admin | Full control |

Add via: Repo → Settings → Collaborators → Add people

---

## 35. GitHub Organizations

An organization is a **shared GitHub account** for teams or companies.

- Repos belong to the org, not one person
- Members can have different roles
- Teams can be created inside orgs with specific permissions
- Good for companies and large open source projects

---

## 36. SSH vs HTTPS

Two ways to connect your local Git to GitHub:

| | HTTPS | SSH |
|-|-------|-----|
| Setup | Easy — just username/token | Requires generating SSH key |
| Authentication | Username + Personal Access Token | SSH key pair |
| Usage | Good for beginners | Preferred for daily use |

**Set up SSH key:**
```bash
ssh-keygen -t ed25519 -C "you@example.com"
# Copy the public key and add it to GitHub → Settings → SSH Keys
```

---

## 37. Git Workflow Strategies

### Feature Branch Workflow (what you are using)
```
main ← staging ← dev ← feature/task
```
- Every task gets its own branch
- PRs merge features into dev
- dev → staging → main when ready

### Gitflow Workflow
Similar but with extra `release` and `hotfix` branches. Used in larger teams.

### Trunk Based Development
Everyone commits directly to `main` frequently with feature flags. Used by big companies like Google.

---

## 38. Common Git Commands Cheat Sheet

```bash
# Setup
git init                          # initialize a new repo
git clone <url>                   # clone a remote repo

# Status & Info
git status                        # show working tree status
git log --oneline                 # compact commit history
git diff                          # show unstaged changes

# Staging & Committing
git add .                         # stage all changes
git add filename                  # stage specific file
git commit -m "message"           # commit staged changes

# Branches
git branch                        # list branches
git checkout -b feature/name      # create and switch to branch
git checkout main                 # switch to main
git merge feature/name            # merge branch into current
git branch -d feature/name        # delete branch

# Remote
git remote -v                     # view remotes
git push origin branch-name       # push to GitHub
git pull origin branch-name       # pull from GitHub
git fetch origin                  # fetch without merging

# Undoing
git restore filename              # discard unstaged changes
git restore --staged filename     # unstage a file
git reset --soft HEAD~1           # undo last commit, keep changes
git revert <hash>                 # safely undo a commit

# Stash
git stash                         # save uncommitted work
git stash pop                     # restore stashed work

# Tags
git tag v1.0.0                    # create a tag
git push origin v1.0.0            # push tag to GitHub
```

---

> This guide covers every major Git and GitHub concept. Work through each section one by one, practice the commands in your repo, and the workflow will become second nature.
