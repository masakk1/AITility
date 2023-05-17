![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/masakk1/AITility?sort=semver&style=for-the-badge)

# WARNING!

1. The docs are not made for Windows! This was made with Linux. A port will be
   done eventually.
2. This is a pre-release and you will encounter errors and nonsense. You can
   help a lot by **opening an issue**.

# Info

## Table of contents

- [Installing](#installing)
- [Using](#using)
  - [Question](#question)
  - [Fix](#fix)
  - [Complete](#complete)
  - [Chat](#chat)
- [About AITility](#about-aitility)
  - [What is AITility?](#what-is-aitility)
  - [Credits](#credits)

## TODO list

> These are just for me, they might change in the future or be removed.

- [ ] Release the binaries directly
- [x] Make use of a custom config file
- [ ] Expand the config file
- [ ] Redesign the fix command
- [ ] Add custom presets
- [ ] Add command aliases
- [ ] Publish to some common distros or package managers
- [ ] Better implementation for requests
- [ ] Adding more AI models
- [ ] Add support for windows
- [ ] Add an option to run a command from a completition

# Installing

Currently the only way to install AIT is building from the main branch directly.
This will change in the future but it's the first release. It's probably a very
bad way of doing it, but it works for now.

To see what packages are going to be installed, check the `setup.py` script.

1. Cloning the repo

```bash
git clone https://github.com/masakk1/AITility
```

2. Building - This is very easy and you don't need to install dependencies
   \
   I will for sure change this later on but it's a first.

> :warning: This has sudo privileges!

```bash
sudo pip3 install .
```

3. After that you can run AIT by typing `aitility` or `ait` on the command line.

```bash
ait question "What does fetching do on git?"
```

# Using

Currently there are 4 commands and two of them have a `--verbose` toggle, which
just means a longer answer.\
Sometimes it will return `retry` a bunch of times and then not answer, running
the same command again usually works. This might get worked on in a future
release.

## Question

AIT will return an answer to the question. It won't remember what you told it if
you ask it again, use the `chat` command for that. This command has a
`--verbose` toggle, if you wish for a longer answer.

> ProTip: If regret not adding `--verbose`, press the up arrow and type
> `--verbose` at the end!

```bash
$ ait question "What is 10 + 5?"
# ╭──────────────────────────────────╮
# │ Bot: The answer to the question  │
# │ "What is 10 + 5?" is 15.         │
# ╰──────────────────────────────────╯
```

## Fix

AIT will try its best to fix the command you've given to it. This is still an
program, and results are not very good on this command.\
This command has a `--verbose` toggle, if you wish for a longer answer.

**TODO: Add code example**

## Complete

Given the command you want to complete, it will return some suggestions.
Currently it only _shows_ the suggestions and you'll have to copy-paste it.

**TODO: Add code example**

## Chat

This command will allow you to enter a chat and have a conversation with the AI.
You can pass a string like with any other command, but it isn't needed.

````bash
$ ait chat
# Write a message or press /quit to quit
# You: How can I print a string in python? Be short
# ╭─────────────────────────────────────────────────────────────────────────────────────╮
# │ Bot: You can print a string in Python by using the print() function. For example:   │
# │                                                                                     │
# │ ```                                                                                 │
# │ print("Hello, world!")                                                              │
# │ ```                                                                                 │
# │                                                                                     │
# │ This will output the string "Hello, world!" to the console.                         │
# ╰─────────────────────────────────────────────────────────────────────────────────────╯
````

# Contributing

If you have problem, question, or suggestion, open an issue! This helps a lot,
specially if you have a prompt preset suggestion.\
Feel free to open a PR, I'll write a CONTRIBUTING.md file eventually.

# About AITility

## What is AITility?

AITility is a tool that allows the user to ask an AI questions. It's for but not
limited to develops, and it comes with some presets by default.

## Credits

- Mas - Owner of this repo, masakk1/AITility
- xtekky - Owner of xtekky/gpt4free
