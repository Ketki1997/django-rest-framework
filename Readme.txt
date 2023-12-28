*****************How to set Virtual Environment***************************
# pip install virtualenv
# python -m venv .env
# cd .\.env\Scripts\
# ./activate

(if while activating your virtual environment you get permission error i.e Execution policy is restricted then open the powershell in Administrator mode and type this command
# Get-ExecutionPolicy
 if the output is Restricted  set it as RemoteSigned or Unstricted
 to set the policy as RemoteSigned or Unstricted type this command
 # Set-ExecutionPolicy RemoteSigned
 and now activate your virtual environment)

********************To install Dependencies from requirement.txt file***************
(go back to the path where requirement.txt file is present  and type the below command)
1) first check your python version by the command below. Your python version should be  3.12.0 or above if not you need to update the version
# python --version

****************Steps to update Python*****************************
1) go to pythons official site https://www.python.org/
2) Click on the Downloads and click on Download python 3.12.0 or the above version
3) Click on the .exe file and click on Run
4) Click on Upgrade Now
5) After successfull updation restart your computer and then check your python --version and then run the below command

# pip install -r requirement.txt

 If while installing requirement.txt file it says could not find the version that satisfies the requirement Django==5.0 or something like this you need to update your python version

********************Database setup*******************************
Steps to install postgres Sql database  and create a new Database StudentDB

1) https://www.postgresql.org/download/windows/
2) Click on Download the installer
3) download the 15.5 PostgreSQL Version for windows
4) Double Click on the .exe downloaded file
5) Click on Next
6) It will Ask to specify the directory where PostgreSQL will be installed (Click on Next)
7) It will ask to select the  component you want to install (select all checkbox and click on Next)
8) It will ask to select a directory under which to store your data (click on Next)
9) Then it will ask for a password for the database superuser (Type Azlogics as your password and click on Next)
10) Please select the port number the server should listen on (Click on Next)
11) select the locale to be used by the new database cluster (Click on Next)
12) the following settings will be used for the installation (click on Next)
13) Setup is now ready to begin installing PostgreSql on your computer (click on Next)
14) It will ask to Launch Stack Builder (Uncheck the checkbox and click on Finish)
15) Go to windows start menu and open PgAdmin4
16) it will ask for the password (Type Azlogics as we have set the password earlier while installing)
17) On the left side there is Servers. Click on server dropdown and left click on Databases  and then click on create then click on  Database and in Database field type StudentDB and click on Save.

# py manage.py makemigrations
# py manage.py migrate


******************* To run the project *****************************
# py manage.py runserver


**** After every  pip install run this command
# pip freeze > requirement.txt



*************** Link to install and understand jwt token ***********

https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html


****************** For solving cors origin issue *************

pip install django-cors-headers

1) add 'corsheaders' in 'INSTALLED_APPS' of settings.py
2) add 'corsheaders.middleware.CorsMiddleware in 'MIDDLEWARE' of settings.py above 'django.middleware.common.CommonMiddleware.
3) add cors allowed origin in settings.py

 CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]