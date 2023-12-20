*****************How to set Virtual Environment***************************
# pip install virtualenv
# python -m venv .env 
# cd .\.env\Scripts\
# ./activate

********************To install Dependencies from requirement.txt file***************
(go back to the path where requirement.txt file is present  and type the below command)
# pip install -r requirement.txt

********************Database setup*******************************
Install PgAdmin4 (i.e postgres Sql database ) and create a new Database StudentDB

# py manage.py makemigrations
# py manage.py migrate


******************* To run the project *****************************
# py manage.py runserver


**** After every  pip install run this command
# pip freeze > requirement.txt