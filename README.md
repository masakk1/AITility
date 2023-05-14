# WARNING! 
1. ONLY THE CHAT WORKS WELL CURRENTLY
2. The docs are not made for Windows! This was made with Fedora Linux. A port will soon be done. 
3. This is a pre-release and you will encounter errors and nonsense. You can help a lot by **opening an issue**.

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
 - [ ] Release the binaries directly 
 - [ ] Make use of a custom config file
 - [ ] Add custom presets 
 - [ ] Add command aliases 
 - [ ] Publish to some common distros 
 - [ ] Better implementation for requests 
 - [ ] Adding more models 
 - [ ] Add support for windows
 - [ ] Add another command to instantly run a command

# Installing
Currently the only way to install AIT is building from the main branch directly. This will change in the future but it's the first release. It's probably a very bad way of doing it, but it works for now.

The dependencies will be installed automatically, the requirements.txt is available if you want to see what is going to be installed. Or open the setup.py to see a more updated version of the dependency list.

1. Cloning the repo
```bash
git clone https://github.com/masakk1/AITility
```

2. Building - This is very easy and you don't need to install dependencies\
I will for sure change this later on but it's a first.
> :warning: This has sudo privileges! 
```bash
sudo pip3 install .
```

3. After that you can run AIT by typing `aitility` or `ait` on the command line, 

# Using
## CURRENTLY ONLY CHAT WORKS WELL NOW.
Currently there are 4 commands and two of them have a `--verbose` toggle.\
Sometimes it will return `retry` a bunch of times and then not answer, running the same command again usually works. 

## Question
AIT will return an answer to the question. It won't remember what you told it if you ask it again, use the `chat` command for that.
```bash
$ ait question "What is 2 + 2?"
# ╭──────────────────────────────────────────────────────╮
# │ Bot: The sum of 2 + 2 is 4.                          │
# ╰──────────────────────────────────────────────────────╯
```
## Fix
This one is under construction! Will be available soon.

**TODO: Add code example**

## Complete
Given this command and the command you want to complete, it will return some suggestions. Currently it only *shows* the suggestions and you'll have to copy-paste it.

**TODO: Add code example**

## Chat
This command will allow you to enter a chat and have a conversation with the AI.
You can pass a string like with any other command, but it's not needed.
```bash
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
```
# Contributing
You can open an issue, I'll work on this later on. Suggestions are welcomed too!

# About AITility
## What is AITility?
AITility is a tool that allows the user to ask an AI questions. It's focused for developers, and it comes with some presets by default.

## Credits
- Masak1 - Owner of this repo, masakk1/AITility
- xtekky - Owner of xtekky/gpt4free
