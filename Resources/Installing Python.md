# Installing Python
### Checking Your Architecture
Are you 32-bit or 64-bit?

Type `cmd` in the Windows Search Bar and select the Program "Command Prompt".

If you haven't already, I recommend pinning this to your taskbar.

Enter this command:
`wmic os get osarchitecture`

You should see something that looks like:
```
OSArchitecture
64-Bit
```

Where 64-Bit could also be `32-Bit`

As of writing the newest version of Python is Python 3.7.0


1. Are you 64-Bit? Get the 64-Bit Version [Here](https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe)
2. Are you 32-Bit? Get the 32-Bit Version [Here](https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe)

If you have an older version of Python, uninstall it.

### Install Python

Run the .exe file you just downloaded. This will launch a Python Setup window.

Before installing, I recommend checking the box that says:

` Add Python 3.7 to PATH`

Run the installation.

Once finished, you'll receive an option in regards to `MAX_PATH`. Accept this option.

### Creating Your First Virtual Environment

The purpose of Virtual Environments is to isolate your packages. This allows you to say, install different versions of the same package without causing conflicts.
You probably won't see this as useful at first, but it's a great habit to get into now.

1. Open Command Prompt

Will use instruct Python to create a new virtual environment. Pick a name that's easy to remember.

I'm going to be installing a virtual environment in `C:\Users\estasney` called perseus.

My command prompt looks like this
```cmd
C:\Users\estasney>_
```

We want to enter this command:
```cmd
python -m venv C:\Users\estasney\perseus
```

So after entering the command, my command prompt looks like this:
```cmd
C:\Users\estasney>python -m venv C:\Users\estasney\perseus
```

Press <kbd>Enter</kbd> to execute. This will take a minute.

### Activating Your Virtual Environment

In order to start working with your Virtual Environment, you must activate it. To do this from command prompt:

1. Navigate to your virtual environment's `Scripts` folder:

```
cd perseus/Scripts
``` 

2. Once there, enter:

`activate`