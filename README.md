# PoojaBlogWebApp
Final project for Code Louisville's May 2021 Session.

For this project, I choose to create a web application using python framework "flask", HTML, CSS, Bootstrap.

Flask is an excellent micro framework that really makes it enjoyable to work with these back-end web application. PoojaBlogWebApp is a blog style of an application where different users can make different posts it can be used for regular blog posts. 

which include following Features:
1.  Read data from an external file, such as text, Images etc  from database 'sqlite:///site.db' and use that data in my application.
2.  Create and call more than 3 functions or methods where at least one of which will return a value that is used somewhere in the code.
3.  Visualize user account, blog post representation of data.
4.  Created a class User, Post and object of that class and populate it with data.
5.  User Management System where we can register new users and users can login.
6.  Update profile pictures which automatically resize when it is uploaded.
7.  Update and delete the post after login.



To run this project you should be considering creating virtual environment by following:
Open the terminal/Cmd and locate the project file.
1.  Setting up virtual environment  
        Python3 -m venv env
2.  Activate environment
        .\env\scripts\activate   - For Windows OS
        source ./env/bin/activate - For Mac OS 
3.  To run this application locally 
        python3 run.py
4.  Copy the URL shown in teriminal and paste it on browser.
5.  To run application on debug Mode
        export FLASK_DEBUG=1    for macos
        set FLASK_DEBUG=1       for windoes OS


Using hashing algorithem for encrypt password  - installing flask-bcrypt