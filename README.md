![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/masakk1/AITility?sort=semver&style=for-the-badge)

# WARNING!
1. You DON'T need any tokens or keys to use ait. This is completely free and open source!
2. The docs are not made for Windows! This was made with Linux. A port will be
   done eventually.
3. This is a pre-release and you will encounter errors and nonsense. You can
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
- [ ] Solve the need for "sudo" and add it to path directly
- [x] Make use of a custom config file
- [ ] Expand the config file
- [ ] Redesign the fix command
- [ ] Add custom presets (custom cmds with presets)
- [ ] Add command aliases
- [ ] Publish to some common distros or package managers
- [ ] Better implementation for requests
- [ ] Adding more AI models
- [ ] Add support for windows
- [ ] Add an option to run a command from a completition or fix

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

Currently there are 4 commands and two of them have a `--verbose` (or `-v`)
toggle, which just means a longer answer.\
Sometimes it will return `retry` a bunch of times and then not answer, running
the same command again usually works. This might get worked on in a future
release.
> 📝 **Note:** Check the EXAMPLES.md for the results!

## Question

AIT will return an answer to the question. It won't remember what you told it if
you ask it again, use the `chat` command for that. This command has a
`--verbose` toggle, if you wish for a longer answer.

> 💡 **ProTip**: If regret not adding `--verbose`, press the up arrow and type `-v` at
> the end!

Here is an example question:

```bash
$ ait question "How can I clone a github repo?"
# or with verbose
$ ait question "How can I clone a github repo?" -v
```

## Fix

AIT will try its best to fix the command you've given to it. This is still an
program, and results are not very good on this command.\
This command has a `--verbose` toggle, if you wish for a longer answer.

Here are some examples:

```bash
$ ait fix "rm aitility/"
# or with verbose
$ ait fix "rm aitility/" -v
```

## Complete

Given the command you want to complete, it will return some suggestions.
Currently it only _shows_ the suggestions and you'll have to copy-paste it.

```bash
$ ait complete "ssh "
```

## Chat

This command will allow you to enter a chat and have a conversation with the AI.
You can pass a string like with any other command, but it isn't needed.

```bash
$ ait chat
# and with an initial prompt
$ ait chat "How can I print a string in python?"
```

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
