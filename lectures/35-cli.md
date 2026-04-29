---
reading: '[Simple BASH Commands](https://en.wikibooks.org/wiki/Bash_Shell_Scripting/Simple_Commands)'
...

# Command Line Interfaces

## CLI

- A CLI is a way to interact with a computer by providing lines of text instructions
- Began to replace punched cards in the 60s as a way to interact with computers

---

![Punched Card](https://upload.wikimedia.org/wikipedia/commons/5/58/FortranCardPROJ039.agr.jpg){height=540px}

---

![Teletype](https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/TTY33ASR.jpg/500px-TTY33ASR.jpg)

## Terminal

- Hardware devices used to send and receive text from a computer
- Includes text output and text input
- Modern systems may include virtual terminals

---

![Computer Terminal](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/DEC_VT100_terminal_transparent.png/960px-DEC_VT100_terminal_transparent.png){height=540px}

## Python REPL

- Accepts and runs Python commands

## Example

```python
>>> a = 5
>>> b = 7
>>> a + b
12
```

## Shell

- Provides an interface to the underlying operating system
- Shells may be graphical or text-based

## Example

- Windows without Explorer

## Text shells

- Many operating systems provide a text-based shell
- Examples include cmd (Windows), Powershell (Windows), and BASH (Unix, Linux, and MacOS)

## Command Format

- Commands are generally entered following a prompt
- Commands may be internal or call an external program
- Parameters are provides by the user for the command

## Example

```sh
> command param1 param2 … paramN
```

## Working Directory

- Running programs (processes) have a current working directory used to resolve relative paths
- The shell may allow the working directory to be changed

## Changing Directories

```bash
cd /home/user/documents
```

## Listing current directory

- It is frequently helpful to be able to list the current directory
- The `ls` command can be used for this in most shells
- Some shells may use `dir`

## Running a program

- One of the key features of a shell is launching programs
- This is accomplished using commands in text-based shells

## Example

Run calculator using Windows:

```cmd
C:\> calc
```

Run thonny using Bash:

```bash
> thonny
```

## Creating scripts

- Begin with shebang: `#!`
- Launch appropriate interpretter

## Bash example

```bash
#!/bin/bash

echo "Hello, world"
```

## Python example

```python
#!/usr/bin/python3

print("Hello, world")
```
