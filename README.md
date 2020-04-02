# Home-Automation

Home automation application used control home smart devices using RestAPI.

##System requirement
    OS              - linux or Mac (Used Ubuntu 18.04)
    Python Version  - Python 3.6
    SQLite          - 3.22
    
##Installation

####SQLite3 installation

    sudo apt-get update
    sudo apt-get install -y sqlite3
   
####SQLite Browser installation(Optional)
    
GUI for sqlite3 database
    
     sudo apt-get install -y sqlitebrowser
     
#### Install python packages

If required you can use virtual environment also. Use this link https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/ to setup virtual environment.

Install application required package

    pip install -r requirements.txt


##Start server

command to setup database

    cd home-automation

Run below comments in directory with have manage.py ((Required to run at first time only))

    python manage.py makemigrations
    python manage.py migrate
      
Starting application server

host - optional default is localhost \
port - optional default is 8000

    python manage.py runserver <host>:<port>

##RestAPI

Using RestAPI call we can able to control and mange home smart devices.

API Details - docs/app_restapi_doc.txt
Sample data - utils/initial_data/app_data.json

##CLI Tool

Using CLI tools are we able control and manage different home smart devices

CLI Tool - home_automation/cli/app_cli.py \
CLI commad details - docs/app_cli_command_doc.txt

##Technologies used

####PyCharm
 
Development tool for python. Very ease and comfortable to develop python application \

####SQLite3
Default database in django and easy use and manage.

####Django framework
One of the best python framework to develop application. In build DB queryset and templete options

##Enhancement plans
1. Add shell script option to start and stop server using CLI tool.
2. Deploy using docker. SO it will easy portable application
3. Enhance to support more smart device and smart device mangement tools (Ex:Resperry pi)
4. Add automated testcases
5. Add setup.py to make this application as installablr python package
6. Create binary for CLI tools

##Notes:
I dont have much experience  in front end so used CLI option as User interactive console.

If any information and clarification contact me.


