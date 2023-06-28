<h1 align="center">My Alias</h1>

<h3 align="center">Alias management help tool for terminal.</h3>

<p align="center">
  <image src="./screenshots/about.png">
</p>

## Install

```bash
  pip install myalias
```

## Setup

```bash

  myalias setup

  # if the path is not defined add the following line to the configuration file
  export PATH="$HOME/.local/bin:$PATH"
```

- ### Commands

  - [help](#help)
  - [add](#add)
  - [remove](#remove)
  - [list](#list)

#### Help

```
  myalias --help

  #return: 

  Usage: myalias [OPTIONS] COMMAND [ARGS]...                                          
                                                                                      
  ╭─ Options ─────────────────────────────────────────────────────────────────────────╮
  │ --version  -v        Show the version and exit.                                   │
  │ --help               Show this message and exit.                                  │
  ╰───────────────────────────────────────────────────────────────────────────────────╯
  ╭─ Commands ────────────────────────────────────────────────────────────────────────╮
  │ add-alias                       Add alias command.                                │
  │ list-alias                      List alias command.                               │
  │ remove-alias                    Remove alias command.                             │
  ╰───────────────────────────────────────────────────────────────────────────────────╯
  ╭─ Help and Others ─────────────────────────────────────────────────────────────────╮
  │ about      Display information about the application.                             │
  │ setup      Setup initial to configure application.                                │
  ╰───────────────────────────────────────────────────────────────────────────────────╯
```

#### Add

```
  myalias add-alias "ll" "description" "ls -la"

  #return:
  Alias created successfully
```

#### Remove

```
  myalias remove-alias "ll" "description" "ls -la"

  # return:
  Alias removed successfully

```

#### List

```
  myalias list-alias

  # return:
  ┏━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
  ┃ Name ┃ Description ┃ Command     ┃
  ┡━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
  │ ll   │ ls -la      │ description │
  └──────┴─────────────┴─────────────┘

```
