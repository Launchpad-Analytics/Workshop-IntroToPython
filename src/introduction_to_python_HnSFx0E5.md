# Introduction to Python

# Session Overview

* * *

This workshop is designed for individuals with little to no experience in Python programming. Participants will learn the basics of Python syntax, including variables, data types, arithmetic and logical operators, control flow statements, and functions. They will also be introduced to Python data structures such as lists, tuples, and dictionaries. By the end of the workshop, participants will have the foundational knowledge to begin programming with Python

  

This workshop is intended for individuals with little to no experience in Python programming. Participants should have basic knowledge of computer programming concepts such as variables and control flow statements.

  

## About Launchpad Analytics

  

Launchpad Analytics is a boutique consulting firm that specializes in modern data analytics tools and capabilities. We also work with expert learning designers to curate world-class technical training experiences across a wide range of tools and topics.

  

[

Launchpad Analytics

Modern data analytics

![](https://www.google.com/s2/favicons?domain_url=https%3A%2F%2Flaunchpadanalytics.carrd.co%2F)https://launchpadanalytics.carrd.co/

](https://launchpadanalytics.carrd.co/)

  

## Support Our Work!

  

[

ko-fi.com

https://ko-fi.com/kellyhopkins

](https://ko-fi.com/kellyhopkins)

  

# Pre-Work

* * *

All of the code for this workshop is located in this GitHub repository:

  

[

GitHub - Launchpad-Analytics/Workshop-IntroToPython: A brief introduction to the Python programming language using Jupyter notebooks

A brief introduction to the Python programming language using Jupyter notebooks - GitHub - Launchpad-Analytics/Workshop-IntroToPython: A brief introduction to the Python programming language using ...

![](https://www.google.com/s2/favicons?domain_url=https%3A%2F%2Fgithub.com%2FLaunchpad-Analytics%2FWorkshop-IntroToPython)https://github.com/Launchpad-Analytics/Workshop-IntroToPython

](https://github.com/Launchpad-Analytics/Workshop-IntroToPython)

  

For this workshop, we will be using two online platforms to run our code - [Google Colab](https://colab.research.google.com/) and [Replit](https://replit.com/), which will prevent you from having to install Python locally on your machine in order to participate. Make sure you have or create both a Google and Replit account (both free) before the start of the session.

  

If you have Python installed on your machine, and you would like to run the workshop materials locally, you can download the repo by clicking the "Clone" button at the top of the page, then clicking "Download ZIP".

![](https://t45028606.p.clickup-attachments.com/t45028606/afe8344a-d92d-4bde-9d9f-933ba94dd52c/image.png)

If you have Git installed on your machine, you can also run the following command in a terminal window to clone the repo locally:

```bash
git clone https://github.com/Launchpad-Analytics/Workshop-IntroToPython.git
```

  

### Other Prep Resources (Optional):

  

Download the latest version of Python:

[

Download Python

The official home of the Python Programming Language

![](https://www.google.com/s2/favicons?domain_url=https%3A%2F%2Fwww.python.org%2Fdownloads%2F)https://www.python.org/downloads/

](https://www.python.org/downloads/)

  

*   Video: Installing Python on Windows
    
      
    
    [https://www.youtube.com/watch?v=yivyNCtVVDk](https://www.youtube.com/watch?v=yivyNCtVVDk)
    
*   Video: Installing Python on Mac:
    
      
    
    [https://www.youtube.com/watch?v=M323OL6K5vs](https://www.youtube.com/watch?v=M323OL6K5vs)
    
      
    
      
    

  

# Workshop Guide

* * *

  

### Part 1: Basic Python Syntax

In this first section of the workshop, we will introduce you to the basics of the Python programming language. Python is a popular programming language known for its simplicity and versatility. We will cover the essential Python syntax and its implementation of basic programming concepts such as variables, data types, operators, and control structures.

  

After covering these foundational concepts, you will be able to understand and write simple Python programs. We will provide you with a Jupyter notebook to guide you through this section of the workshop. Jupyter notebooks are interactive documents that allow you to write and run Python code in your web browser.

  

To follow along with the workshop, you will need to have access to the Jupyter notebook. We recommend that you open the notebook in Google Colab, which is a cloud-based platform for writing and running Jupyter notebooks. You can easily open the notebook by clicking on the provided link and then selecting the "open in Colab" button:

  

  

[

Workshop-IntroToPython/01 - Python Syntax.ipynb at main · Launchpad-Analytics/Workshop-IntroToPython

A brief introduction to the Python programming language using Jupyter notebooks - Workshop-IntroToPython/01 - Python Syntax.ipynb at main · Launchpad-Analytics/Workshop-IntroToPython

![](https://www.google.com/s2/favicons?domain_url=https%3A%2F%2Fgithub.com%2FLaunchpad-Analytics%2FWorkshop-IntroToPython%2Fblob%2Fmain%2F01%2520-%2520Python%2520Syntax.ipynb%23enroll-beta)https://github.com/Launchpad-Analytics/Workshop-IntroToPython/blob/main/01%20-%20Python%20Syntax.ipynb#enroll-beta

](https://github.com/Launchpad-Analytics/Workshop-IntroToPython/blob/main/01%20-%20Python%20Syntax.ipynb#enroll-beta)

  

### Part 2: Python Scripting and Practice Scenarios

  

For the second half of this workshop, we will be moving from our notebook environment to a more traditional coding environment where we will learn how to write Python scripts. If you're already familiar with IDEs, feel free to follow along in your editor of choice (remember to clone the repo!) For the rest of us, we will be using Replit for the remainder of this workshop.

  

If you didn't get a chance to create your Replit account at the beginning, feel free to do so now. Once you're logged in, create a new blank repl with the [official Python template](https://replit.com/@replit/Python?v=1). Click through the guide below for step-by-step instructions:

  

[https://scribehow.com/embed/Creating\_a\_New\_Repl\_on\_Replitcom\_\_h68vfDmGTAKIpzQKe8WJvA](https://scribehow.com/embed/Creating_a_New_Repl_on_Replitcom__h68vfDmGTAKIpzQKe8WJvA)

####   

In the middle pane of the window, there is a blank Python file that is called `main.py` . At its core, a Python file is just like any other plain text file (i.e. `.txt` files), but the `.py` file extension tells us that the file contains a script, or set of functions, written in Python that are to be carried out by a machine running the Python programming language. Unlike a notebook, where chunks of code are separately run in cells, running a Python script executes all of the code from top to bottom. When code is saved in a script, that script can then be used to perform tasks repeatedly and independently, allowing you to automate time-consuming manual tasks and processes.

  

Before we get into some more complex scripts, let's revisit the "Hello World" exercise from the beginning of the workshop. We will start by adding the `print()` statement to the first line of the `main.py` file:

  

```python
print("Hello, World!")
```

  

Next, you can run the code by either pressing the green "Run" button at the top of the page, or pressing `Ctrl + Enter` on your keyboard. You will see the output of the code you ran show up in the right pane under the "Console" tab:

  

![](https://t45028606.p.clickup-attachments.com/t45028606/90d2b298-acee-4bc2-a45a-b6f3df0f3e38/image.png)

  

The console is a computer terminal window where a user enters commands, or "inputs", and can view the results of the computer carrying out those commands (the "outputs."). Because we selected a Python environment when we created the Repl, our console is a Python console that only accepts Python commands as input.

  

We can also make our scripts interactive by allowing the user to provide information to the program via the terminal/console window. For example, let's write a program that asks the user what their name is, and then greets them by name. we can use the `input()` function in Python to get user-entered information from the console.

  

```python
#get user name
name = input("Please enter your name:")

#form greeting
greeting = "Hello, {}!".format(name)

#greet user
print(greeting)
```

![](https://t45028606.p.clickup-attachments.com/t45028606/267d44fd-fe7b-4835-a013-8612940ea782/image.png)

  

  

When the user enters their name, their response is saved under the variable `name` which is used to form the greeting. In the second line of code, we are using what's called "string formatting" to customize the greeting to use whatever name or text the user entered.

  

As a last step in this example, we will have our Python program display the current time after it greets the user. Python has a set of functions that help us work with dates and times that come with the `datetime` module, but those functions aren't immediately available to us like `print()` and `input()` are. We need to use an `import` statement to bring the module into our coding environment. Once we've done that, we can use the `date.today()` function to get today's date, then use the `.strftime()` method to represent the date in our desired format.

  

```python
from datetime import date

#get user name
name = input("Please enter your name:")

#form greeting
greeting = "Hello, {}!".format(name)

#greet user
print(greeting)

#get today's date
today = date.today()
formatted_date = today.strftime("%B %d, %Y")

print("Today is " + formatted_date)
```

  

![](https://t45028606.p.clickup-attachments.com/t45028606/bac31fb2-8ece-4651-844b-7475d733b706/image.png)

  

#### Interacting with the Shell

  

![](https://t45028606.p.clickup-attachments.com/t45028606/81ffa04b-eee7-4d45-9d57-66a1e960134c/image.png)

  

In the right pane along with the Console tab, you will also find a tab for the Shell, which is another computer terminal that gives you access to a broader scope of computer resources and tools. The shell interpreter carries out instructions in a language called Bash, and is often referred to as the command line. For every action that you can perform on a computer through its Graphical User Interface (GUI), there is a terminal command that can perform the same function. For example, let's look at the list of files that are in our Repl environment:

  

![](https://t45028606.p.clickup-attachments.com/t45028606/75538689-9e3c-4007-9d5e-457e2d68b534/image.png)

Similar to the File Explorer on a physical computer, we can get a list of files that are located on that machine. From the terminal, we can also get a list of files in the current working directory (the folder that we're currently looking at) by entering the command `ls` :

  

![](https://t45028606.p.clickup-attachments.com/t45028606/d0adefc4-1710-4102-b2b8-2bb2178ad08b/image.png)

  

The terminal can also be used to view the contents of a file without having a graphical text editor like the one in the middle pane. The contents of any text file can be printed to the screen using the `cat` command:

![](https://t45028606.p.clickup-attachments.com/t45028606/8b65bd8d-0919-401c-8432-1baeb7239dd1/image.png)

  

In order to have the shell interpreter run the code that's in our Python script, we have to instruct it to use the Python program to carry out the instructions located in the `main.py` by running the following command:

  

```plain
python main.py
```

  

The keyword `python` is the main command here which is telling the interpreter the specific program to use, and the filename is entered after in order to provide information that the program need to operate, which in this case is the Python file we want to run. When the Python script is run, we can observe identical results to when we ran the script using the console:

  

![](https://t45028606.p.clickup-attachments.com/t45028606/4afe88d2-5f08-499d-96c9-7b7e0d890274/image.png)

Note: you can also start a Python console in your shell window by simply running the `python` command.

  

Not only is the terminal used to interact with files and resources on your local machine, but it can also carry out instructions to interact with online files and systems. Remember the Github repository that we used to access the Jupyter notebook during the intro sections? That repository also contains all of the files we need for the rest of the workshop, so we need to download those files and save them inside of our Repl.

  

Copy the files in the repository directly into your Repl by running the `git clone` command and specifying the web address of the repository:

  

```bash
git clone https://github.com/Launchpad-Analytics/Workshop-IntroToPython.git
```

  

Once the process is finished, you will now see all of the new files listed in your Repl:

  

Throughout the rest of this workshop, we will be looking at 3 scenarios where a Python script can be used to automate a task:

1. File Automation: Combining separate Excel files into one workbook + calculating summary statistics
2. Getting Data From the Web: making an API call to extract data from an online data source.
3. Webscraping: Extract specific information from the HTML of a website (useful when website does not provide a direct data download link).

  

### Exercise #1: Excel Automation

  

> **Scenario:** Each department in your company manages their office supply purchases in their own spreadsheet, which is stored on the company shared drive (located in the `02 - Exerecise/` folder). At the end of each month, the office manager has to calculate the purchases across all departments and report the totals.

  

In this exercise, there are three Excel files located within the project directory, each containing a list of purchased office supplies along with the unit price for each:

  

![](https://t45028606.p.clickup-attachments.com/t45028606/2bf676e2-83e5-46eb-9db1-d9106909bd6e/image.png)

![](https://t45028606.p.clickup-attachments.com/t45028606/35e946dd-0000-4991-b2b7-15f0571112cf/image.png)

If you are unable to view the spreadsheets in your online coding environment, you can download the files and view them locally in Excel or Google Sheets.

  

In the shell window, use the `cd` command to navigate to the `02 - Exercise` folder:

```bash
cd Workshop-IntroToPython/02\ -\ Exercise/
```

  

Create a new Python file in this directory, either by using the UI, or by using the `touch` command in the shell. Name this file `excel_report.py` .

  

```bash
touch excel_report.py
```

  

In order to work with these spreadsheets using Python, two packages are needed that don't come automatically installed - `pandas` and `openpyxl` . The packages will need to be [installed](https://packaging.python.org/en/latest/tutorials/installing-packages/) in your Python environment and [imported](https://realpython.com/lessons/import-statement/) at the top of your script.

  

[Pandas](https://pandas.pydata.org/docs/index.html#) is one of the most popular data analysis packages for Python, and is often the standard for working with tabular data. We will use Pandas to read our excel files into memory as a `DataFrame` object and perform a variety of tasks with the data.

  

Use the `pd.read_excel()` function to read in the first spreadsheet, storing the value in the variable `deptA` .

  

```python
deptA = pd.read_excel("dept_A_purchases.xlsx")
```

  

Once you have your `deptA` dataframe, you can use some common Pandas function to get a quick overview of the information it contains. For example, the `.head()` command outputs the first 5 rows of the table, which can also be printed to the console.

  

Write the command to run the Python script from the shell.

  

*   `excel_report.py` checkpoint:
    
    ```plain
    import pandas as pd
    ```
    

  

![](https://t45028606.p.clickup-attachments.com/t45028606/246ecfaf-90b5-4fe4-89a2-ff51ac30d2a8/image.png)

  

After running the script, the first five lines of the table, along with the column names and row numbers are printed to the console. This is often the first step to performing any kind of data analysis, as it's important to inspect the dataframe for any data or import errors.

  

What other questions can we ask about our data? Perhaps we want to know how many purchases were made, the order total, or the most expensive items that were bought. Below are some Pandas functions that can accomplish each task:

  

*   `.count()` - Returns the number of rows contained in a single or set of columns
*   `.sum()` - Calculates the numerical sum of a set of values (i.e. a column)
*   `.sort_values()` - Sorts a dataframe based on the values of one or more columns

  

Adding to your script, calculate the total number of purchases, the overall order total, and the most expensive item purchased. **Print each calculation to the console.**

  

Refer to the [Pandas documentation](https://pandas.pydata.org/docs/getting_started/overview.html) for help with these functions.

  

*   `excel_report.py` checkpoint:
    
    ```plain
    import pandas as pd
    ```
    
      
    

  

![](https://t45028606.p.clickup-attachments.com/t45028606/7d1f7d08-c74a-403c-ac22-3aa702f46a05/image.png)

  

Now that we've seen how Pandas can work with Excel spreadsheets, we will use it to read in each department's purchases, calculate a summary for each department, and combine each file into one multi-sheet spreadsheet. Create a new Python script in the current exercise folder called `combine_excel.py` . At the top of the file, import both `pandas` and `openpyxl` like last time.

  

Using the `pd.read_excel()` function, read in each of the department purchases spreadsheets, saving them to their own variable

  

*   `combine_excel.py` checkpoint:
    
    ```python
    import pandas as pd
    ```
    

  

In addition to the 3 dataframes that will make of each sheet of our combined spreadsheet, we also want a summary tab that will display the total purchases for each department. There are many ways in which you can make spreadsheet calculations in Python, but to keep this example simple, we're going to make a dataframe containing those calculations and then write that table directly to a sheet using the code below (copy the snippet and paste it into your script):

  

```plain
summary = pd.DataFrame({
    "Summary": "",
    "Dept A purchases": dept_a_purchases["price"].sum(),
    "Dept B purchases": dept_b_purchases["price"].sum(),
    "Dept C purchases": dept_c_purchases["price"].sum(),
}, index=range(1)).T
```

  

Next we're going to use these 4 dataframes to make one combined spreadsheet by using the `pd.ExcelWriter()` function, which uses `openpyxl` as a dependency. In Python, reading and writing data from files requires a connection to be established to a particular file, which can affect performance if not managed properly. A context manager can be created with the `with` command in order to properly open and close a file once the script is done with it. Within this context manager, each dataframe is written to a different sheet of a new spreadsheet using the `pd.to_excel()` function:

  

```plain
with pd.ExcelWriter('all_purchases.xlsx') as writer:
    summary.to_excel(writer, sheet_name="Summary")
    deptA.to_excel(writer, sheet_name="Dept A")
    deptB.to_excel(writer, sheet_name="Dept B")
    deptC.to_excel(writer, sheet_name="Dept C")
```

  

Now that the `combine_excel` script is complete, run the script from the command line and verify that the new spreadsheet has been created. Download and inspect the generated file.

  

*   `combine_excel.py`
    
    ```python
    import pandas as pd
    ```
    

  

### Exercise #2: Introduction to APIs and Automating Data Extraction

  

In today's digital age, businesses and developers increasingly rely on the efficient exchange of data between different applications and systems. This is where Application Programming Interfaces, or APIs, play a vital role.

  

**What are APIs?**

An API, short for Application Programming Interface, is a set of rules and protocols that allow different software applications to communicate and interact with each other. It serves as an intermediary layer that enables the exchange of data and functionality between systems, even if they are built on different technologies or platforms.

  

Think of APIs as a messenger that delivers your request to a service or application and returns the response you need. They provide a standardized way for software components to interact, making it easier to build applications that leverage existing functionalities and data from external sources.

  

One of the most powerful use cases for APIs is automating data extraction tasks. In the past, extracting data from websites, databases, or online services required manual effort and often involved copying and pasting information. With APIs, however, you can programmatically retrieve data in a structured and automated manner, saving time and reducing errors. APIs allow you to connect with third-party services, platforms, and applications, such as social media platforms, payment gateways, or weather data providers. By integrating these APIs into your workflow, you can extract relevant data and incorporate it into your own application or process.

  

In this next example, we will explore the fundamentals of making API calls, discuss different types of APIs, and learn practical techniques for automating data extraction tasks. So let's dive in and explore some APIs!

  

### Analyzing API Data

  

Take a look at the dataset and read through the documentation:

  

[

data.cityofnewyork.us

https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95

](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95)

  

Discussion Questions:

*   How many columns are there? Which columns do you find the most interesting?
*   What does each row in this dataset represent?
*   How many rows/records are contained in the dataset?

  

Supplemental Discussion: What is the source of this data?

  

Suggested listening: the history of the NYPD CompStat program:

[

open.spotify.com

https://open.spotify.com/episode/7vPVmqFCFxBZJpStDAHl2n

](https://open.spotify.com/episode/7vPVmqFCFxBZJpStDAHl2n)

  

### Pull API data with Python script - `wget`

  

On the dataset homepage, find the URL of the API endpoint, and specify "CSV" as the format option. Copy the API endpoint to use when you build your script.

  

![](https://t45028606.p.clickup-attachments.com/t45028606/9e8035ed-eb4d-4468-a667-3cc7a2400b76/image.png)

  

In the `03 - Exercise/` directory of the workshop repo, open the `pull_nyc_crash_data_v1.py` file. Follow the instructions in the comments to write a script that pulls the crash data from the API endpoint and saves is to a file named `nyc_crashes.csv` . Your script should print a success message to the console after the file has been downloaded.

  

For this exercise, you will need to install and import the [wget](https://pypi.org/project/wget/) package into your script and use the `wget.download()` function to both request and save the data from the API endpoint:

  

```python
file = wget.download(url=url_endpoint, out="nyc_crashes.csv")
```

  

*   `pull_nyc_crash_data_v1.py` solution:
    
    ```python
    # import wget module
    ```
    

  

### Pull and filter data with `requests` package

  

The [Requests](https://pypi.org/project/requests/) package is one of the most popular Python packages due to its power and ease of use. For this next exercise we will use this package to pull JSON data from the API, then use the Pandas to filter for only the crashes that took place in Manhattan.

  

First, open the `pull_nyc_crash_data_v2.py` file and follow the instructions in the comments to start building the script.

  

On the dataset homepage, copy the API endpoint, specifying JSON as the data format:

  

![](https://t45028606.p.clickup-attachments.com/t45028606/1431f120-3a81-4861-a166-dcb818c1141c/image.png)

  

Use the `requests.get()` function to make a request to the API endpoint, saving the API response to the variable `res` :

  

```python
res = requests.get(url_endpoint)
```

  

Inspect the `res` variable that holds our Response object and see what different pieces of information it holds. To get the raw JSON data from the API response, use the `.json()` method and create a new pandas dataframe with the output.

  

```plain
crashes = pd.DataFrame(res.json())
```

  

Filter the dataframe for only the crashed that happened in Manhattan, and export those rows to a csv file. (Hint: use the "borough" column to filter the data)

  

```python
manhattan_crashes = crashes[crashes["borough"] == "MANHATTAN"]
```

  

*   `pull_nyc_crash_data_v2.py` solution:
    
    ```python
    # import requests and pandas packages
    ```
    

  

### Exercise #3: Webscraping

  

For websites that don't have an easy way to extract their data, such as with an API for file download option, web scraping is a powerful way to get any needed information. When you scrape a website, you are downloading the HTML and other code included with the site and parsing through the extracted information in a procedural way in order to isolate the desired data points. In Python, [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/) is the most popular web scraping library that we will be using to extract structured information from some simple web pages.

  

Take a look at this simple webpage that displays a grid of countries and some basic information about each:

  

[

www.scrapethissite.com

https://www.scrapethissite.com/pages/simple/

](https://www.scrapethissite.com/pages/simple/)

  

_It is recommended that you use the Chrome browser to follow along with the instructions for this exercise, but you can use any modern browser that has developer tools_

  

Using the Chrome browser, press the F12 key to open the developer tools panel. Ensure that the "Elements" tab is selected

  

![](https://t45028606.p.clickup-attachments.com/t45028606/d08ca83f-d921-430f-8761-f51f9a8c0f2c/image.png)

  

Scroll through the list of HTML elements and look for the parts of the webpage that get highlighted. Once you find the element that contains the body of the page, drill down to the different elements that hold more granular parts of the webpage until you find the elements related to country information

  

![](https://t45028606.p.clickup-attachments.com/t45028606/18fea8ad-38ba-41a3-82e4-25f7b9f9336a/image.png)

_Take note of identifying information related to the elements you want to scrape, such as specific class names and ids._

  

Open the `scrape_countries_v1.py` file in the `04 - Exercise` directory, following the instructions in the comments. Using the `requests` package, extract the HTML from the page using its URL.

  

```python
page = requests.get(url)
```

  

  

Create a new `BeautifulSoup` parser object based on the extracted HTML code from the webpage, saving it to a new variable `soup` :

  

```plain
soup = BeautifulSoup(page.content, "html.parser")
```

  

By using the developer tools tab, we can see that each country to located in a div with a class of "col-md-4 country". Use this class name with the `.find_all()` method to generate a list of all matching elements.

  

```plain
x = soup.find_all("div", {"class":"col-md-4 country"})
```

  

Create a for loop to iterate through each country's div element and parse out the countries name. Save the name to a variable and print it to the console. Pick another element for each country to print with each loop.

  

*   `scrape_countries_v1.py` checkpoint:
    
    ```python
    # import BeautifulSoup, pandas, and requests modules
    ```
    

  

Additional Exercises:

Using the same grid of countries, write a script that creates a csv file of all of the countries and their details

*   `scrape_countries_v2.py` solution:
    
    ```python
    # import BeautifulSoup, pandas, and requests modules
    ```
    

  

Write a script to extract the table of hocket stats from the below webpage and export the data to a csv.

_Hint: Use the Pandas function_ `pd.read_html()` to easily convert an HTML table into a dataframe.

*   `scrape_hockey.py` solution:
    
    ```python
    from bs4 import BeautifulSoup
    ```
    

  

##   

# Wrap Up

* * *

  

We did it

![](https://media0.giphy.com/media/ae6m4ljnl69urJ539F/200.gif?cid=a7595362l7cof26il4qyixc7daqpkuh5zvzzy4mz1z6x79fd&ep=v1_gifs_search&rid=200.gif&ct=g)

  

[https://2nbi2f0n9zm.typeform.com/to/DEQEQ4j6](https://2nbi2f0n9zm.typeform.com/to/DEQEQ4j6)

  

## Additional Resources

* * *

  

### Interactive Python tutorials:

  

W3Schools:

[

Python Tutorial

W3Schools offers free online tutorials, references and exercises in all the major languages of the web. Covering popular subjects like HTML, CSS, JavaScript, Python, SQL, Java, and many, many more.

![](https://www.google.com/s2/favicons?domain_url=https%3A%2F%2Fwww.w3schools.com%2Fpython%2F)https://www.w3schools.com/python/

](https://www.w3schools.com/python/)

  

Datacamp:

[

www.datacamp.com

https://www.datacamp.com/courses/intro-to-python-for-data-science

](https://www.datacamp.com/courses/intro-to-python-for-data-science)

  

[learnpython.org](http://learnpython.org):

  

[

Learn Python - Free Interactive Python Tutorial

learnpython.org is a free interactive Python tutorial for people who want to learn Python, fast.

![](https://www.google.com/s2/favicons?domain_url=https%3A%2F%2Fwww.learnpython.org%2F)https://www.learnpython.org/

](https://www.learnpython.org/)

  

  

Video Python Courses:

  

[https://youtu.be/eWRfhZUzrAc](https://youtu.be/eWRfhZUzrAc)

  

[https://www.youtube.com/watch?v=H1elmMBnykA](https://www.youtube.com/watch?v=H1elmMBnykA)