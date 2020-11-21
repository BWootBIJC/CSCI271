# CSCI271
This project scrapes the "best rated" pc parts from newegg.com. The choices to pick from as of now are GPUs, CPUs, Motherboards, or Monitors.

First you will want to install a text editor. I prefer to use visual studio code or pycharm to run the project.
When using vs code, you may have to install a python code runner plugin. This link will show you how to do that: 
https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner 

When you download the project, you will need to make sure you have the following installed:
Python, django, requests, beatifulsoup4

Here is how you download each of those.

Python - Go to https://www.python.org/downloads/ and install python version 3.8
Django - Within the terminal of vs code or pycharm, type the following command: python -m pip install Django
Beautiful Soup 4 - Same steps as django except the command is, pip install beautifulsoup4
Requests - Same steps as django except the command is, python -m pip install requests

After you have installed those libraries, you should then be able to run the project.
To run it via terminal, type the command, python manage.py runserver

After you run the runserver command, the following output should display on the terminal:
November 21, 2020 - 13:28:40
Django version 2.2.16, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

After you see the message saying "Starting development server at http://127.0.0.1:8000/, you want to copy that url and enter it in your browser of choice.
After you run it in the browser, it will take you to a page with a dropdown menu of the following pc parts, "GPU", "CPU", "Motherboard", and "Monitor".
After you select one of those options and hit submit, you will see the output in the terminal on whichever editor you are using. 
So, after submitting your choice, you will need to return to the text editor to see the results. 
