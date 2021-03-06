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
***
![](https://thumbs.gfycat.com/AnimatedGrossIslandcanary-size_restricted.gif)
***

- [ ] Install *pandas* and *easygui*

#### Finish with import

With pandas and easygui now installed, you should import them. Your file will now look like:

```Python
import os
import csv
import pandas
import easygui
```

In no particular order.

#### Where's that folder?

Here's where you will appreciate *easygui*. We will write a line that displays a *Directory Open Box* popup where we can select the folder with the CSV files.

Now's a good time to mention you can grab these files [Here](https://github.com/estasney/Master_Builders/raw/master/Resources/Files/combine_these.zip). There are 40 files in total in a compressed (zipped) folder. By now you should know how to unzip them or at least how to Google how to do it.

#### A Method to This Madness

To get *easygui* to do something useful, we need to access one it's *methods*. If you were a package you might have methods such as:

``` Python
master_builder.eat()
master_builder.build()
```

Think of methods as a logical grouping of actions. We can also provide initial instructions to methods. So if your eat() method contains instructions on the proper way to eat food, it would be important to specify what food you are about to eat, right? Same for your .build()
method. We should probably specify what materials we have at hand and what we want our creation to look like.

``` Python
master_builder.eat(food_type='pizza')
master_builder.build(raw_materials=['Wood', 'Steel'], creation='baseball_bat')
``` 

Let's slow down a moment. First you'll notice that I'm including quite a few <kbd>_</kbd> in my object names. That's a good habit to get into as it makes it much more readable. Also, you cannot include <kbd>Space</kbd>s within an object name.

See the raw_materials **argument** for master_builder.build? Rather than specify one material, I specified multiple materials with a **list**. Think of a list as a flexible container that can hold multiple variables.

If we want to create an object ```work_week``` we might define the days of the week within a list like:

``` Python
work_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
```

Since each day of the week is a **string**, it is surrounded with either single <kbd>'</kbd> or double <kbd>"</kbd>. **string** is just a technical term for text.
We start a list with: 

<kbd>[</kbd>
 
and end it with <kbd>]</kbd>.

Each item with the list is separated with a <kbd>,</kbd>.

With these core concepts, we can now access *easygui* and its diropenbox() method.

Now your file can look like this:

``` Python
import os
import csv
import pandas
import easygui

folder_to_open = easygui.diropenbox()
print("The folder you selected is: " + folder_to_open)
```

You can run the file and see a popup appear! Note that the popup may be buried underneath other open windows but it's there!

And now once you select the folder, you will see the message contained within ```print``` that displays the folder that you selected to open.

#### The Beauty of Loops

Did you ever have to write the same sentence hundreds of times as punishment for something you did in grade school?

You likely got very bored and tired of the tedious, boring work. But our computers are excellent at these kinds of things!

Whether they should perform the same task hundreds or even billions of times, once they have a set of instructions, you are done!

So keep in mind, our spreadsheets that we need to combine can be ten or ten million. The amount of work required of you to combine these is the same (so long as the instructions apply to every file)

#### Your First Loop

First we should tell the computer what spreadsheets we want to combine. Fortunately for us, all of these spreadsheets are in one folder.

So we will give instructions saying, "Do <something> for every file in this folder." We accomplish this with the *os* package (and you should save this for future reference, you'll use it again.)

``` Python
import os

list_of_spreadsheets = [] # Creating an empty list that we will populate with filenames

for file in os.listdir(folder_to_open):  # file can be any variable you like, even pizza
    # Note the indentation here, you use the TAB key
    file_path = os.path.join(folder_to_open, file)
    list_of_spreadsheets.append(file)  # Append is adding one item at a time to our list
   
# Note that there is now no indentation. Code at this point and below only executes after our for loop is complete
number_of_files = len(list_of_spreadsheets)  # Use len() to get the length of something. In this case how many items.
number_of_files = str(number_of_files)  # Since we want to print number_of_files, we use str() to convert an integer to string.
print("Found " + number_of_files + " spreadsheets in the folder")
        
```

**Note**: The introduction of .append(), len() and str()

#### Open and Combine

We now have a list of files with their direct paths. Now we just need to write instructions saying, "For each of these files, open the file and add the contents to a running list"

For opening CSV files, I prefer *pandas*. You're under no obligation to do so, but it will make your life easier!

Let's get these combined!

``` Python

# Continuing from above...

first_sheet = pd.read_csv(list_of_spreadsheets[0]) # We pull our first sheet from the list of files.

# For the remaining spreadsheets we will add each new spreadsheet to our first_sheet. To avoid repeating the first
# spreadsheet note the use of the range function.

total_sheets = len(list_of_spreadsheets)

for file_number in range(1, total_sheets): # Setting range at 1 rather than 0 skips our first sheet
    file_to_open = list_of_spreadsheets[file_number]  # file_number changes by + 1 with each loop
    sheet_contents = pandas.read_csv(file_to_open)
    first_sheet = first_sheet + sheet_contents
    

```

There was a lot going on there! But what we've done is to open the first spreadsheet and then add every spreadsheet (except the first one) to this first sheet.

The result is our combined spreadsheets.

#### Save our work

This is even easier... let's skip the csv package and use just the pandas package.

We need to set a save path so we'll use easygui to get that

```file_save_path = easygui.filesavebox()```

And the rest is cake:

``` first_sheet.to_csv(file_save_path)```







```




 


