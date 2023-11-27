Git
=====

Software Size
-------------

- One way to measure software size is via source lines of code (SLOC)
- A modern piece of large software, such as an operating system, may have tens of millions of lines of code

Team Size
---------

- Some software is developed by indviduals
- Many applications developed by large teams
- Thousands of developers may work on large application such as Windows or the Linux kernel

---

How can we help thousands of people work together to write millions of lines of code?

Version Control
---------------

- Version control systems are used to manage change to the source code of software systems
- These tools become critical as the size of software and teams increases

History
-------

- Version control systems manage history of the codebase
- Mistakes can be undone
- Previous versions of the software can be used

Git
---

- Distributed version control system
- Original developed to manage the source code of the Linux kernel
- Most widely used version control system today

Init
----

- We can create a new git repository using `git init`
- This creates the `.git` metadata directory
- This repository will have no commits or pointers to commits

Commits
-------

- At its core, git track states of the system known as commits

---

![Git commits](https://git-scm.com/book/en/v2/images/snapshots.png)


Staging
-------

- Before files are commited, they must be staged

---

![Git lifecycle](https://git-scm.com/book/en/v2/images/lifecycle.png)

---

![Git areas](https://git-scm.com/book/en/v2/images/areas.png)
