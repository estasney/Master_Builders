# Introduction to Python
## Table of Contents





### Installing Python

#### 32 or 64 Bit?
Before getting started you should determine if you have a 32-bit or 64-bit PC. While 32-bit installations will work on 64-bit PC's, you are limiting yourself.

Note that 64-bit will not run on 32-bit machines.

You can find if your machine is 32-bit or 64-bit by visiting: [How do I know what bit version of windows I have?](https://www.howtogeek.com/howto/21726/how-do-i-know-if-im-running-32-bit-or-64-bit-windows-answers/)

#### Python 2 or Python 3?
If you need to ask, the answer is **Python 3**. 

#### Where do I download Python?

Python | Version 
 --- |--- | 
[Python 3](https://www.python.org/ftp/python/3.6.2/python-3.6.2-amd64-webinstall.exe) | 64-Bit
[Python 3](https://www.python.org/ftp/python/3.6.2/python-3.6.2-webinstall.exe) | 32-Bit

#### How do I "open" Python?
While you could run and access Python after installation, you'll want to have an IDE (Integrated Development Environment).

For this course, I will recommend Pycharm Community Edition. It can look a little intimidating at first but don't worry you'll come to love it.

[Pycharm Community Edition - Free](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)

#### How do I use Pycharm?

[Here](https://www.jetbrains.com/help/pycharm/migrating-from-text-editors.html) is an excellent guide from Pycharm

## Commence Coding!

*As we work through the coding challenge I will introduce concepts*

#### Task
You have been asked to combine 40 spreadsheets of varying length but with identical columns into one spreadsheet. While you could manually copy and paste them together, that sounds really boring. Also there's a good chance you could miss a file.

### Code Your Way Out
#### Getting Started

1. Create a New Project In PyCharm. Name it what you will.
2. Create a new Python File (.py). Name it what you will, but something along the lines of combining CSV files.

#### Import Built-In Packages

Recall that in Python, you can think of packages as "apps". There are numerous packages to choose from and all are free and open-source.

At the top of your file, write 
```Python
import csv
```
The *csv* package is *built-in*. That means it comes pre-installed with Python and there is no need to download it.

The *csv* package will allow us to read and write csv files. While we could work with Excel files, the proprietary nature of Excel makes things more difficult than need be.

Next, write
```Python
import os
```

Again, this is a built-in package no need to download and install it. The *os* package will let us work directly with the file system of our computers.

#### Install Packages

I'd like to share two packages that I discovered only after several months. First, *easygui* is great for making your program interactive and flexible enough to handle minor changes. 
Since we'd like to not have to manually edit our code each time the CSV file location changes, we'll leverage *easygui* and its File Selection Feature

Secondly, *pandas* will save you quite a great deal of time when importing CSV files. While it's geared more for serious number crunching and can quickly get complicated, you'll see how easy it is to use for this scenario.

Now, how do I install these?
<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>A</kbd> while you have PyCharm open. And enter Project Interpreter

![](https://thumbs.gfycat.com/AnimatedGrossIslandcanary-size_restricted.gif)


 


