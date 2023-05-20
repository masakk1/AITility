# About this file

1. All of this are literally copy-paste of the original nothing has been taken
   out. I don't even know what it says myself lmao.
2. Because this is a copy-paste, all the formatting is missing. You won't see
   it's pretty colors or formatting here.
3. The borders might look weird, so I recommend making your window size bigger
   or zooming out if that happens.

This is kind of test file, so I can make sure everything is OK or if it's not.
Anyway everything should be in here! Happy coding!

## Question

```
$ ait question "How can I clone a github repo?"
╭─────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                              AIT:                                               │
│                                                                                                 │
│ To clone a GitHub repo, you can use the git clone command followed by the URL of the repo. Here │
│ is an example:                                                                                  │
│                                                                                                 │
│                                                                                                 │
│  git clone https://github.com/username/repo-name.git                                            │
│                                                                                                 │
│                                                                                                 │
│ Replace username with the GitHub username of the repo owner, and repo-name with the name of the │
│ repository you want to clone. This command will create a copy of the repo on your local         │
│ machine, in a subdirectory with the same name as the repo.                                      │
│                                                                                                 │
│ Note that you need to have Git installed on your machine in order to use this command.          │
╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### with verbose option on

```
$ ait question "How can I clone a github repo?" -v
╭─────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                              AIT:                                               │
│                                                                                                 │
│ To clone a GitHub repository, you can use the git clone command in the terminal. Here are the   │
│ steps:                                                                                          │
│                                                                                                 │
│  1 First, navigate to the directory where you want to clone the repository using the cd         │
│    command.                                                                                     │
│  2 Next, open the repository on GitHub in your web browser, and click on the green "Code"       │
│    button. You'll see a dropdown menu with an HTTPS URL for cloning the repository. Copy that   │
│    URL.                                                                                         │
│  3 Go back to your terminal and enter the following command:                                    │
│                                                                                                 │
│                                                                                                 │
│   git clone <https-url-of-the-repository>                                                       │
│                                                                                                 │
│                                                                                                 │
│ Replace <https-url-of-the-repository> with the actual URL you copied in step 2. So the final    │
│ command might look something like this:                                                         │
│                                                                                                 │
│                                                                                                 │
│   git clone https://github.com/myusername/my-repo.git                                           │
│                                                                                                 │
│                                                                                                 │
│  4 Press enter and wait for the repository to clone. The files will be downloaded into a new    │
│    directory with the name of the repository.                                                   │
│                                                                                                 │
│ That's it! Now you have a local copy of the repository that you can edit and work with.         │
╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Fix

This one is currently a WIP so your results might be either really good or
really bad. In this case, it was okay.

```
$ ait fix "rm aitility/"
╭─────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                              AIT:                                               │
│                                                                                                 │
│ Command: rm aitility/                                                                           │
│                                                                                                 │
│ Possible Error: rm: cannot remove 'aitility/': Is a directory                                   │
│                                                                                                 │
│ Possible Fix: Use the -r option to remove a directory and its contents recursively, like this:  │
│ rm -r aitility/. Alternatively, you can use the rmdir command to remove an empty directory.     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### with verbose option on

Same problem as the normal option. It was okay here, too.

```
$ ait fix "rm aitility/" -v
╭─────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                              AIT:                                               │
│                                                                                                 │
│ Please be aware that the command rm is a potentially dangerous command that can permanently     │
│ delete files and directories. Please proceed with caution and make sure you have backups of     │
│ important data.                                                                                 │
│                                                                                                 │
│ Assuming you want to remove the directory called aitility, you can use the following command:   │
│                                                                                                 │
│                                                                                                 │
│  rm -r aitility/                                                                                │
│                                                                                                 │
│                                                                                                 │
│ The -r flag is necessary to delete a directory recursively, including all its subdirectories    │
│ and files. If you just want to delete a file, you can use the following command:                │
│                                                                                                 │
│                                                                                                 │
│  rm filename                                                                                    │
│                                                                                                 │
│                                                                                                 │
│ Where filename is the name of the file you want to delete.                                      │
│                                                                                                 │
│ Make sure you are in the correct directory when you run the rm command, and verify the files    │
│ you are deleting before running the command to avoid accidental deletions.                      │
│                                                                                                 │
│ Let me know if you need further assistance.                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Complete

```
$ ait complete "ssh "
╭─────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                              AIT:                                               │
│                                                                                                 │
│ Uncompleted command: ssh                                                                        │
│                                                                                                 │
│  1 ssh user@host (Connect to host with specified user)                                          │
│  2 ssh -p port user@host (Connect to host on specific port with specified user)                 │
│  3 ssh-keygen (Generate a new SSH key pair)                                                     │
│  4 ssh-copy-id user@host (Copy SSH public key to remote host for passwordless access)           │
│  5 sshfs user@host:/remote/path /local/path (Mount remote directory on local system using SSH)  │
│                                                                                                 │
│ Note: Replace "user" and "host" with the appropriate values for the specific SSH connection you │
│ want to make.                                                                                   │
╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Chat

As a chat, it works like any chatbot, except the fact it has internet support.

```
$ ait chat "How can I print a string in python?"
Chat mode activated.
Write a message or press /quit to quit
You: How can I print a string in python?
╭─────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                              AIT:                                               │
│                                                                                                 │
│ To print a string in Python, you can use the print() function and enclose the string in either  │
│ single quotes or double quotes. Here is an example:                                             │
│                                                                                                 │
│                                                                                                 │
│  my_string = "Hello, world!"                                                                    │
│  print(my_string)                                                                               │
│                                                                                                 │
│                                                                                                 │
│ This will output the string "Hello, world!" to the console. You can also use triple quotes to   │
│ create a multi-line string. Here is an example:                                                 │
│                                                                                                 │
│                                                                                                 │
│  my_string = """This is a multi-line                                                            │
│  string in Python"""                                                                            │
│  print(my_string)                                                                               │
│                                                                                                 │
│                                                                                                 │
│ This will output:                                                                               │
│                                                                                                 │
│                                                                                                 │
│  This is a multi-line                                                                           │
│  string in Python                                                                               │
│                                                                                                 │
│                                                                                                 │
│ Alternatively, you can use f-strings to embed variables within the string. Here is an example:  │
│                                                                                                 │
│                                                                                                 │
│  name = "Alice"                                                                                 │
│  age = 25                                                                                       │
│  print(f"My name is {name} and I am {age} years old.")                                          │
│                                                                                                 │
│                                                                                                 │
│ This will output "My name is Alice and I am 25 years old." to the console.                      │
╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
You:
```
