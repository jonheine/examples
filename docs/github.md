Here is some information about Github. There is a lot here but this should give
you an overview. I wrote this kind of quickly so if you need help let me know. 

A "Repository" is just a way to keep a bunch of files together. It contains
history so you can go back and look at what has changed when. With a repository
you typically make changes to the source code then "Commit" the changes to the
repository so it knows about what was changed. There are many different
repositories, just like there are different text editors or word processors. It
is mainly what you are used to. I work with 3 or 4 different ones at work.

 "Git" is the repository that is the most popular right now. Git was written by
the creator of Linux. He wanted something that was open source and worked well
for people working remotely. Typically when you "Clone" (make a copy) of a git
repository, you get the latest version of all the files and it also stores the
history behind how each file changed. The history is stored in a hidden
directory called ".git".

With git, one person's repository is the "Master" repository. This is "The
latest and the greatest" version of the project. If I grab a copy of someone
else's repository and make changes, I have to share those changes back to the
"Master" repository so other people can see them.

GitHub is another piece of software. It is a web site that holds a bunch of
"Master" repositories. It is currently owned by Microsoft. Anyone can go to
http://github.com and create their own free account. From there you can create
a repository to hold a bunch of files that you want saved. On the Github site,
there are millions of repositories that you can browse and pull down code. I
have my own account and pushed up a few repositories.

If you browse tohttps://github.com/jonheine/examples

This is a repository that I am setting up so we can share some example
programs. You can poke around and look at the files and see the history. If you
want to "use" the files, you will need to "Clone" them locally. You then get a
copy. To do this you need a "Client".


=== Git Client ===
To use git you need client software. There are many different versions of the
client software. The two that I use most are one called "Git for Windows" and
another called "TortoiseGit".  The former is kind of command line driven and is
a bit harder to use, the TortoiseGit works on windows and is probably a good
version for you. To get it go here: https://tortoisegit.org/download/  Pull
down the 64 bit version and have it install on your computer.

Once installed, use windows explorer (the file browser) to create a directory
somewhere on your computer. A "Source" directory on your desktop is fine (I
almost always create a c:\Src directory and put stuff there).  Browse to that
directory and Right Click and that will bring up a "Context Menu". In that menu
you should find something like "Git Clone". When you choose it, it will pop up
a dialog asking for a repository name, you can type
in: https://github.com/jonheine/examples.git . After hitting OK, it will create
an examples directory with my code in it (and all the magic .git files to give
you history). The right click menu has other "Git" programs that you can use to
see history, do differences, ...  I can explain more if you get this far.

A typical usage would look like this.
1) I find a repository with code I like.
2) I "Clone" the repository to my computer.
3) I test out the software
4) I make some changes to some of the files.
5) I check the code in "commit" (Note this checks things on your local computer).
6) I then "Push" my changes back to the "Master" repository.

There is also a "Pull" command that updates your repository with changes that
others have made to the Master repository. I do this all day long, although we
do not use GitHub for our internal source code, we have our own servers at
work.

Here are a few example repositories that are interesting. 

This is a repository that is updated every day with covid 19 counts. The data
files are Comma Separated Fields (.CSV) files that have a count of the number
of cases in every county in the US. I wrote a python script to read the data
and show me the cases in Washington.
https://github.com/nytimes/covid-19-data.git 

Here is python code that somebody wrote to generate Jazz
https://github.com/jisungk/deepjazz.git

Here is the source code for the Linux Operating system.
https://github.com/torvalds/linux.git





