To run this project, you will need to:


1. Clone the project to your local machine.
2. Create a virtual environment and activate it.
3. Install the project's dependencies.
4. Run the Django development server.

<!-- Here are the detailed steps: -->

1. Clone the project to your local machine.
Open a terminal window or command prompt and navigate to the directory where you want to clone the project. Then, run the following command:
`git clone https://github.com/yusraa99/Ads-Project-Django.git`
This will clone the project to a new directory called `Ads-Project-Django`.

2. Create a virtual environment and activate it.
A virtual environment is a sandboxed environment that allows you to install and run Python packages without affecting your system-wide Python installation. To create a virtual environment, run the following command:
`python -m venv venv`
This will create a new virtual environment called `venv` in the current directory. To activate the virtual environment, run the following command:
`Scripts\activate`


3. Install the project's dependencies.
The project's dependencies are listed in the `requirements.txt` file. To install the dependencies, run the following command:
`pip install -r requirements.txt`
This will install all of the project's dependencies into the virtual environment.

4. Run the Django development server.
To run the Django development server, run the following command:
`python manage.py runserver`
This will start the Django development server on port 8000. You can now access the project by visiting `http://localhost:8000` in your web browser.


## Additional tips
Here are a few additional tips for running a Django project from GitHub:
* If you are using a Windows machine, you may need to use the `venv\Scripts\activate` command instead of the `source venv/bin/activate` command to activate the virtual environment.
* If you are using a Mac, you may need to use the `source venv/bin/activate` command instead of the `venv/Scripts/activate` command to activate the virtual environment.
* If you are using a Linux machine, you may need to use the `source venv/bin/`
* If you use SQLite you should change some of database settings such as NAME (name of Database), USER, PASSWORD
* If you use PostgreSQL you should change some of database settings such as NAME (name of Database), USER, PASSWORD