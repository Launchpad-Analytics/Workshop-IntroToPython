# Functions, Files, and Scripts

In this module, we're going to learn how to take the Python syntax we learned and give it legs.

# Session Setup
During this session, we're going to utilize more of the features in our Google Colab environment. If you utilized colab for the first session's notebook, you can keep that same notebook active. If not, you can start a new Colab session by following this link*: [New Notebook](colab.new)

(**Alternatively, if you chose to set up your local Python coding environment, you can follow along with your local environment. If you're not working with a linux system, then some of the command line inscructions may be different*)

We won't actually need the notebook for most of this session (you can still use it for scratchwork), so we're going to configure our view by opening a Terminal tab and extending it so that it takes up most of our screen. The Terminal button can be found in the bottom-left corner of the screen:

<img width="1916" height="952" alt="image" src="https://github.com/user-attachments/assets/31818590-0984-4eba-8a0b-d75cef8d78fc" />


When you're done, your Colab window might look something like this:
<img width="1918" height="944" alt="20260711-0252-35 7921598" src="https://github.com/user-attachments/assets/af2a705c-5b6c-48ab-a9c8-e539975d7113" />

## What is a terminal? Quick command line demo
A terminal is a text-based user interface that allows a user to access a computer system's resources... (TODO: FINISH EXPLANATION)

Here are some basic bash commands that you can run from the command line:

### Where am I? Use `pwd` to print your "working directory", or what folder you're currently inside of
<img width="314" height="164" alt="image" src="https://github.com/user-attachments/assets/7413f45b-a8d7-4c31-9658-3875cb731d8c" />

We are currently inside the `/content` folder, which is the default folder for the Colab environment.

### What's in here? Use `ls` to list all of the files in the current directory
<img width="280" height="150" alt="image" src="https://github.com/user-attachments/assets/97899847-34df-4ca6-b06f-45233aad4216" />

Running `ls` from the `content/` directory tells us that the only thing inside of our current working directory is another directory called `sample_data/`. To quicky see what's inside of this nested directory, we can pass it to the ls command like this:

`ls sample_data/`

This lists all of the files in this lower directory without having to navigate to it:
<img width="1074" height="188" alt="image" src="https://github.com/user-attachments/assets/290c6d29-de69-43ed-b2db-a5c2e798c9de" />

This `sample_data/` folder contains some popular practice datasets for machine learning, which Colab has included in the standard environment.

Similarly, we can also list the files that are in a higher level directory than our current working directory by using `ls ..`

<img width="910" height="212" alt="image" src="https://github.com/user-attachments/assets/17d60280-d33d-4349-9270-34319c73fb57" />

## Download the practice files by cloning the workshop repo

# Creating our first script:
In this context, a script is a file that houses a series of Python commands to be carried out in a sequential order... (TODO: Finish intro)

Using our same terminal window, we're going to create an empty python file with the following command:

```bash
touch good_morning.py
```

After a rief moment, your new python file should appear in the files list on the left. Double-click the script file to open it in a new tab. The terminal tab will be hidden by this new file, but you can drag it down below the script file to split the window if it suits your preference:

<img width="1916" height="938" alt="image" src="https://github.com/user-attachments/assets/d79e2f57-fe6b-482a-9f42-5a5eb826e338" />

To start, we're going to create as basic of a script as we can. We're going to create a single string variable `name`, and then print a custom greeting message using whatever name is passed to that variable:

```python title
# good_morning.py

name = "Kelly"

print("Good Morning, " + name + "!")
```
Next, we're going to run our script by running this command in our terminal:

```
python good_morning.py
```

After running, out output should look like this:

<img width="362" height="142" alt="image" src="https://github.com/user-attachments/assets/d9d9a82b-94f8-407e-a989-726c0bfc59d0" />

There's often many different ways to achieve the same result in programming, and each method may be better suited for what you want to accomplish. The concatenating of the text strings to build our message works well, but we can also use what's called an **f-string** to create better string templates and embed values directly. We're going to do that now with our print statement:

```python
name = "Kelly"

print(f"Good Morning, {name}!")
```

# Example Build: Personal Assistant Wake-up Message
<img width="60%" height="30%" alt="image" src="https://github.com/user-attachments/assets/89cf51de-70bd-4a78-858f-db74ea7deb64" />


- Start with blank .py file
- Run basic lines of code
- add functions
- error handling + try/except
- look at example helper script
- import script functions as module
- build new script on top of it
- argparse

