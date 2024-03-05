<h1 align="center">My Alias</h1>

<h3 align="center">Alias management help tool for terminal.</h3>

<p align="center">
  <image src="https://github.com/thiagomeloo/myalias/blob/main/screenshots/about.png">
</p>

## Install

```bash
  pip install myalias
```

## Update

```bash
  pip install myalias --upgrade
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
  - [import](#import)
  - [remove](#remove)
  - [list](#list)

#### Help

```bash

  myalias --help

  #return: 

  Usage: myalias [OPTIONS] COMMAND [ARGS]...                                          
                                                                                      
  ╭─ Options ─────────────────────────────────────────────────────────────────────────╮
  │ --version  -v        Show the version and exit.                                   │
  │ --help               Show this message and exit.                                  │
  ╰───────────────────────────────────────────────────────────────────────────────────╯
  ╭─ Commands ────────────────────────────────────────────────────────────────────────╮
  │ add-alias       Add alias to the application. Args:     name (str): Name of       │
  │                 command.     description (str): Description of command.           │
  │                 command (str): Command to execute.                                │
  │ import-aliases  Import list aliases to the application. Args:     file_path       │
  │                 (str): Path to aliases list file.                                 │
  │ list-alias      List alias to the application.                                    │
  │ remove-alias    Remove alias to the application. Args:     name (str): Name of    │
  │                 command.                                                          │
  ╰───────────────────────────────────────────────────────────────────────────────────╯
  ╭─ Help and Others ─────────────────────────────────────────────────────────────────╮
  │ about      Display information about the application.                             │
  │ setup      Setup initial to configure application.                                │
  ╰───────────────────────────────────────────────────────────────────────────────────╯
```

#### Add

```bash
  myalias add-alias "ll" "description" "ls -la"

  #return:
  Alias created successfully
```

#### Import

```bash

  myalias import-aliases ./echoAliases

  #return:
  Adding alias ec
  Alias created successfully

```

#### Remove

```bash
  myalias remove-alias "ll" "description" "ls -la"

  # return:
  Alias removed successfully

```

#### List

```bash

  myalias list-alias

  # return:
  ┏━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━┓
  ┃ Name ┃ Description ┃ Command ┃
  ┡━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━┩
  │ ll   │ description │ ls -la  │
  └──────┴─────────────┴─────────┘


```
