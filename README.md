# portfolio

## Using Flask

First make your own virtual environment:

IN your preferred IDE ( mine: pycharm)

use new project name it Web ( I named mine as so)
and in the terminal 

PS C:\Web> cd ..
PS C:\> python -m venv Web
PS C:\> Web\Scripts\activate

// I observed an error saying that this is restricted for my laptop so I fixed it by going to my p
powershell terminal as an administrator 

Get-ExecutionPolicy -List

and it was showing that all were allsigned
so i put the following command 

Set-ExecutionPolicy RemoteSigned

and typed A

To make it remotesigned 

Definitions:
Restricted – No scripting allowed
Unrestricted – You can run any script, No signing is required.
RemoteSigned – Good for Test, Dev environments. Only files from the internet need to be signed. This is the default setting on servers.
AllSigned  – local or remote script – It should be signed by a trusted publisher.


# Read more: https://www.sharepointdiary.com/2014/03/fix-for-powershell-script-cannot-be-loaded-because-running-scripts-is-disabled-on-this-system.html#ixzz7xTKFgcMi

Now,
PS C:\> Web\Scripts\activate
(Web) PS C:\> python -m Flask run 
C:\Web\Scripts\python.exe: No module named Flask

//I realized i did not install flask in my current directory

(Web) PS C:\> pip install flask
Collecting flask
  Using cached Flask-2.2.3-py3-none-any.whl (101 kB)
Collecting click>=8.0
  Us.......
(Web) PS C:\> $env:FLASK_APP = "server.py"
(Web) PS C:\> flask run                   
'FLASK_ENV' is deprecated and will not be used in Flask 2.3. Use 'FLASK_DEBUG' instead.
server
'FLASK_ENV' is deprecated and will not be used in Flask 2.3. Use 'FLASK_DEBUG' instead.
'FLASK_ENV' is deprecated and will not be used in Flask 2.3. Use 'FLASK_DEBUG' instead.
 * Serving Flask app 'server.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [30/Mar/2023 15:18:47] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [30/Mar/2023 15:18:55] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [30/Mar/2023 15:40:56] "GET / HTTP/1.1" 200 -


To turn on debugger in powershell

(Web) PS C:\> $env:FLASK_APP = "server.py"  
(Web) PS C:\> $env:FLASK_ENV = "development"
(Web) PS C:\> flask run

Used the following for the html, css files. 
© 2017 Free HTML5 Template. All Rights Reserved.
Designed by FreeHTML5.co Demo Images: Unsplash

CSS and JAVA script are static files 

rgba(255, 144, 0, 0.9);
used this instead rgb(243, 99, 99)

## DEPLOYMENT

Using PythonAnywhere I deployed the files.   
