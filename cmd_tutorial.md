# Linux Command Line

## Introduction
The command line is an invaluable tool for any aspiring hacker. While it lacks the beauty and visual appeal of a graphical user interface (GUI), it more than makes up for that with its efficient simplicity. The intent of this guide is to help bring CTF beginners up to useable speed for CTFs. As a result, there are a lot of features of the command line that we have opted to leave out.

## A Brief History
We will often use different names to refer to the command line, namely shell, command line, and terminal. The name terminal arose from the beginnings of computers when individual users would have to use a computer to connected to a mainframe in order to run commands. The endpoint was called the terminal, and its only objective was to send commands to the mainframe and print the result it received back. Since graphics weren't around yet, everything was text-based. Additionally, bandwidth was precious and sending more letters took up more of it, so developers created shorter commands to minimize bandwidth consumption. Both of these traditions have carried through the decades, and now we have software terminals and short commands, such as `cp` rather than `copy`.


Note: We will be using Ubuntu 18.04 for this guide

## Basic Navigation
Okay, so we've opened up the terminal application for the first time, and we're greeted with a line similar to this:
```
arch1t3ct@init6ctf:~$
```

from here, we can type in our commands and obtain a result
```bash
arch1t3ct@init6ctf:~$ whoami
arch1t3ct
arch1t3ct@init6ctf:~$ 
```

But how do we know "where" we are on our computer? Fortunately, we have a command for that: `pwd`
```bash
arch1t3ct@init6ctf:~$ pwd
/home/arch1t3ct
arch1t3ct@init6ctf:~$ 
```

What this tells us is that we are in the arch1t3ct folder inside of the home folder, but unless you know more about the linux filesystem layout, that isn't very helpful. Much like windows, linux has a root directory from which all other directories are stored. Windows uses `C:\` while linux uses `/`. When we see any directory path that starts with `/`, we call it an `absolute path`
```bash
arch1t3ct@init6ctf:~$ pwd
/home/arch1t3ct
arch1t3ct@init6ctf:/home$ cd /home
arch1t3ct@init6ctf:/home$ pwd
/home
```
After `c`hanging `d`irectories to `/home`, we can check our `p`resent `w`orking `d`irectory to see where we are again. Typing out the absolute path of every directory we want to visit would quickly become tedious, so `relative paths` were introduced to prevent repetition. Knowing that we are in `/home` and there is a directory named `arch1t3ct`, we can jump right to it.
```bash
arch1t3ct@init6ctf:/home$ pwd
/home
arch1t3ct@init6ctf:/home$ cd arch1t3ct
arch1t3ct@init6ctf:~$ pwd
/home/arch1t3ct
```

The key thing to notice here is that we didn't have to write
`cd /home/arch1t3ct`
because we were already in the `/home` directory.

Alright, so far we've introduced the root directory structure and the following commands:

Change Directory (`cd`)\
Present Working Directory (`pwd`)

While both are useful, they don't allow us to do anything interesting. In fact, we don't even know what is in each folder/directory. We can remedy this with the `ls` command. The purpose is to `l`i`s`t the contents of a directory. However, if we run the command right now, we'll be sorely disappointed:
```bash
arch1t3ct@init6ctf:~$ ls
arch1t3ct@init6ctf:~$
```
We got nothing?? Well.. there's nothing to show right now. We can always get more information by adding additional arguments to the `ls` command. Personally, I always run the command as `ls -lsa`
```bash
arch1t3ct@init6ctf:~$ ls -la
drwxr-xr-x 3 arch1t3ct arch1t3ct 4096 Jul 29 14:55 ./
drwxr-xr-x 4 root      root      4096 Jul 29 14:55 ../
-rw-r--r-- 1 arch1t3ct arch1t3ct  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 arch1t3ct arch1t3ct 3771 Apr  4  2018 .bashrc
-rw-r--r-- 1 arch1t3ct arch1t3ct  807 Apr  4  2018 .profile
drwx------ 2 arch1t3ct arch1t3ct 4096 Jul 29 14:55 .ssh/
arch1t3ct@init6ctf:~$
```

Wow, that gives us a lot of information, most of which doesn't make sense... Lets step through each piece one at time:


| permisions |links|owner|group|filesize|modification|filename
|---|:---:|---:|---:|---:|---:|---:|---:|
| drwxr-xr-x | 3 | arch1t3ct | arch1t3ct | 4096 | Jul 29 14:55 | ./ |   

We'll get more into permissions later, but this is who can do what with the file.\
links tells us the number of links to the file.\
Owner and Group detail who owns the file and what group the file is a part of respectively.\
filsize is the size of the file.\
Last modification time is when the file was last edited or changed.\
Lastly, the filename tells is what the file is called.

You're probably wondering why all of this information is showing up now instead of before. Well, any filename that starts with a `.` is considered "hidden" and won't appear normally. the `-a` option in `ls` will show `a`ll files. Similarly, the `-l` option will put the output in `l`ong format.

This wraps up Basic File System Navigation. We hope you found it informative and helpful.

## File Manipulation

At this point in the tutorial, we're going to delve into how to actually do things with files. We'll be covering the following commands:
```bash
touch
cp
mv
rm
mkdir
rmdir
file
chmod
```
We're going to start with `touch` because it allows us to create empty files which will help us with the rest of the commands.

```bash
arch1t3ct@init6ctf:~$ touch hello.txt
arch1t3ct@init6ctf:~$ ls -l 
total 0
-rw-rw-r-- 1 arch1t3ct arch1t3ct     0 Jul 31 13:17 hello.txt
```

As you can see, there is now a `hello.txt` with a size of 0 bytes. 
The `cp` and `mv` commands are very useful and straightforwad. Both follow the same command format:\
```cp <source> <destination>```

cp makes a copy with without destroying the original and mv will move the file (and rename it) and delete the original.
Here is a demo of the two commands:
```bash
arch1t3ct@init6ctf:~$ cp hello.txt hello_world.txt
arch1t3ct@init6ctf:~$ ls -l
total 0
-rw-r--r-- 1 arch1t3ct arch1t3ct 0 Jul 31 13:18 hello.txt
-rw-r--r-- 1 arch1t3ct arch1t3ct 0 Jul 31 13:21 hello_world.txt
arch1t3ct@init6ctf:~$ mv hello_world.txt goodbye_world.txt
arch1t3ct@init6ctf:~$ ls -l
total 0
-rw-r--r-- 1 arch1t3ct arch1t3ct 0 Jul 31 13:21 goodbye_world.txt
-rw-r--r-- 1 arch1t3ct arch1t3ct 0 Jul 31 13:18 hello.txt
```
deleting a file is as easy as `rm` for `r`e`m`ove:
```bash
arch1t3ct@init6ctf:~$ rm goodbye_world.txt
arch1t3ct@init6ctf:~$ ls -l
total 0
-rw-r--r-- 1 arch1t3ct arch1t3ct 0 Jul 31 13:18 hello.txt
```

so we can make a ton of files now, move them around, and remove them, but we have no way to organize them. They all just sit in a single directory. We can create our own directories to help deal with that using `mkdir <directory name>`!

```bash
arch1t3ct@init6ctf:~$ mkdir organize
arch1t3ct@init6ctf:~$ ls -l
total 0
-rw-rw-rw- 1 arch1t3ct arch1t3ct   0 Jul 31 18:11 hello.txt
drwxrwxrwx 1 arch1t3ct arch1t3ct 512 Jul 31 18:11 organize
```

We can tell that organize is a directory because the first field in the permissions section is a `d` instead of a `-`. So we've decided that we don't really need to use this directory and don't want to clutter our workspace with it so we can remove it with `rmdir`

```bash
arch1t3ct@init6ctf:~$ rmdir organize
arch1t3ct@init6ctf:~$ ls -l
total 0
-rw-rw-rw- 1 arch1t3ct arch1t3ct   0 Jul 31 18:11 hello.txt
```

So now, we have a small toolbox of builtin commands that are helpful to navigate and do operations on the command line, but there are a couple more that we'd like to introduce.

The first of which is `file`. This handy command will tell you what kind of file a specific file is which can be very helpful in determining how to respond to it in a CTF. The syntax is simple: `file <filename>`. Below, we've demonstrated a couple of examples.

```bash
arch1t3ct@init6ctf:~$ file hello.txt
hello.txt: empty
arch1t3ct@init6ctf:~$ file organize
organize: directory
arch1t3ct@init6ctf:~$ file /bin/ls
/bin/ls: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=3f60bd5f1fee479caaed0f4b1dc557a2086d3851, stripped
arch1t3ct@init6ctf:~$ file /home/arch1t3ct/.bashrc
/home/arch1t3ct/.bashrc: ASCII text
```

Lastly, we'd like to introduce file execution and changing permissions. When you get a binary during a CTF, you'll need to execute it as part of the exploit or reversing process. To do so, you type the path to the binary or, if you're in the same directory that you have stored the binary in, you can run `./<binary name>`

```bash
# This example is the absolute path
arch1t3ct@init6ctf:~$ /home/arch1t3ct/hello
Hello, world!
# This example is the relative path
arch1t3ct@init6ctf:~$ ./hello
Hello, world!
```

Now, when you get a binary from a CTF and you try to run it the first time, you'll probably see something like:
```bash
arch1t3ct@init6ctf:~$ ./hello
-bash: ./hello: Permission denied
```

To understand why, lets take a look at the permissions
```bash
arch1t3ct@init6ctf:~$ ls -l ./hello
-rw-rw-rw- 1 arch1t3ct arch1t3ct 16608 Jul 31 18:41 hello
```

particularly, we're going to focus on `-rw-rw-rw-` and what it means.
The first `-` is whether or not the file is a directory or different file. If it is a directory, it would be a `d` instead, and it has nothing to do with the permissions of the file itself. The remaining 9 fields, however, are permissions settings.

There are actually 3 groups of 3. The division of permissions is into User, Group, and Others where User is the owner of the file, Group is the group the file belongs to, and Others is everyone else that doesn't fall into those two categories. The applicable permissions are `R`ead, `W`rite, and e`X`ecute. So the output of the above command tells us that Users, Group members, and Others can all `r`ead and `w`rite to the file, but none of them can e`x`ecute it. Fortunately, we have a command that lets us alter the permissions on the file: `chmod` which is short for `ch`ange `mod`e, and the syntax is: `chmod <permissions to add or remove> <filename>`\
But what do permissions look like in the context of adding or removing them. Well, You can control which division receives the permission changes. For example, lets allow the User to execute the file:
```bash
arch1t3ct@init6ctf:~$ chmod u+x hello
arch1t3ct@init6ctf:~$ ls -l hello
-rwxrw-rw- 1 arch1t3ct arch1t3ct 16608 Jul 31 18:41 hello
```

We specifically gave the `u`ser permission to e`x`ecute the file but no one else. We can also grant everyone permission to execute by not specifying the who the permission change affects

```bash
arch1t3ct@init6ctf:~$ chmod +x hello
arch1t3ct@init6ctf:~$ ls -l hello
-rwxrwxrwx 1 arch1t3ct arch1t3ct 16608 Jul 31 18:41 hello
```

We can also prevent Others from executing if its a sensitive file:

```bash
arch1t3ct@init6ctf:~$ chmod o-x hello
arch1t3ct@init6ctf:~$ ls -l hello
-rwxrwxrw- 1 arch1t3ct arch1t3ct 16608 Jul 31 18:41 hello
```

## Piping and Redirection

Wow, we're really beginning to craft a nice small toolbox for the linux command line, but there are still a lot of powerful, yet simple things we can do that will improve our ability to use the terminal. Here, we'd like to cover some more tools and concepts like:
```
Ouput redirection
Piping
grep
pagers(less, more, head, tail)
```
Okay, so you're looking at all those things and wondering what the heck they all are which is perfectly reasonable.

Let's start with output redirection. This means that instead of printing the output of a command, we want to send it to a file. This is useful for when we need the output later or its too large to print all at once. We can do this using `>` and `>>`.

`>` overwrites the contents of the target file while\
`>>` appends to the end of the file preserving the contents already there. Both redirects will create the target file if it doesn't already exist.
For demo purposes, we'll use the `echo` command which just echoes the input back to the user. Here's a demo of redirects:

```bash
# This creates the output.txt file and adds the first line
arch1t3ct@init6ctf:~$ echo "First line!" > output.txt
arch1t3ct@init6ctf:~$ cat output.txt
First line!
# This overwrites the output.txt file with new contents
arch1t3ct@init6ctf:~$ echo "Overwrite!" > output.txt
arch1t3ct@init6ctf:~$ cat output.txt
Overwrite!
# This appends the echoed string to output.txt
arch1t3ct@init6ctf:~$ echo "Second line appended!" >> output.txt
arch1t3ct@init6ctf:~$ cat output.txt
Overwrite!
Second line appended!
```

Woohoo! Time to move on to pipes. What the heck does that mean?? Well, the `|` character is called a pipe and its purpose on the command line is to take the output from one command and feed it to the input of another command. This is really useful for a lot of commands but to demonstrate it, we will search for a string within a file.

We already know how to read a file using `cat`, now its time to search a file using `grep`. `grep` is a useful, tool for finding strings within a file. The origins of `grep` are pretty far back and a useless bit of trivia is that grep stands for '`g`et `r`egular `e`xpression `p`rint'. 

Say we have a massive file like this one:

```bash
arch1t3ct@init6ctf:~$ ls -l rand.txt
-rw-rw-rw- 1 arch1t3ct arch1t3ct 1836938 Jul 31 19:35 rand.txt
```
If we try and just read it, our screen will be FILLED with the data and we'll never find what we want. But say we know that we're looking for a string containing the word "flag" in the file, we can read the contents of the file using `cat` and simultaneously search using `grep`:

```bash
arch1t3ct@init6ctf:~$ cat rand.txt | grep flag
flag{youre_gonna_be_leet}
arch1t3ct@init6ctf:~$ 
```
The best part is our screen is nice and clean! `grep` is a really powerful tool, and I strongly recommend learning to use it to its full potential. 

## Editing Files
## Extras