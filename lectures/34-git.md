# Git

## Software Size

- One way to measure software size is via source lines of code (SLOC)
- A modern piece of large software, such as an operating system, may have tens of millions of [lines of code](https://en.wikipedia.org/wiki/Source_lines_of_code#Example)

## Team Size

- Some software is developed by individuals
- Many applications are developed by large teams
- Thousands of developers may work on large application such as Windows or the Linux kernel

---

How can we help thousands of people work together to write millions of lines of code?

## Version Control

- Version control systems are used to manage change to the source code of software systems
- These tools become critical as the size of software and teams increases

## Google Docs

## History

- Version control systems manage history of the codebase
- Mistakes can be undone
- Previous versions of the software can be used

## Git

- Distributed version control system
- Originally developed to manage the source code of the Linux kernel
- Most widely used version control system today

## Init

- We can create a new git repository using `git init`
- This creates the `.git` metadata directory
- This repository will have no commits or pointers to commits

## Status

- `git status` can be use to check the current state of the repository

## Example

```
> git init
Initialized empty Git repository...
> git status
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

## Commits

- At its core, git track states of the system known as commits

---

![Git commits](https://git-scm.com/book/en/v2/images/snapshots.png)

## Staging

- Before files are committed, they must be staged

## Add

- `git add` can be used to track and stage a file

## Example

```
> git add main.py
> git status
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   main.py
```

## Commit

- `git commit` can be used to create a new commit
- The `-m` flag can be used to provide a message
- File names can be provided
- The `-a` flag will commit all changes

## Log

- `git log` can show the commit history

---

![Git areas](https://git-scm.com/book/en/v2/images/areas.png)
