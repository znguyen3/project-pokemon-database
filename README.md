# CMSC-461-Project

CMSC 461
Database Management Systems, TERM PROJECT

Professor: Lawrence Sebald

Group Members:
Zachary Nguyen

Pokedex Database Project

System Requriments:
- MySQL
- MySQL Workbench
- PyCharm

You would need to download a MySQL Connector in Pycharm in order to run this program by enabling Python 
programs to access MySQL databases using an API that is compliant with the Python Database API Specification:
- To install, in Pycharm, go to File, Settings and go to the 'Project Interpeter' under the 'Project: Name of
the ProjectFile'
- Add a specific package called "mysql-connector-python"

Things to note before running the program:
- Inside main.py, the arguments in mysql.connector, connect() only relates to what I used and will need to 
change depending on what the user set up in their own MySQL and MySQL Workbench
- (host='localhost'). I used my host
- (user='root'). The user will be the username of the user used when installing and setting up MySQL
- (password = 'sqlzach01$'). Password would be what the user setup when installing SQL, if the password is 
different than the one I was using ('sqlzach01$'), the password would need to be changed to what they set their 
password as
- (port='3306'), If the port that the user is running on is different than what the user is running on in 
MySQL Workbench and MySQL Connections, the user would need to change the port number to what their running on
- (database='pokedex_project'). Is the database in MySQL WOrkbench that Pycharm is connecting to

To check, view the MySQL Connections in MySQL Workbench that the database sql file is imported, to see what connection requirements needs to be changed 
depending on how the user sets up the MySQL and MySQL Workbench

How to run code:
- Install MySQL Workbench and MySQL server
- Download the repository of main.py and in MySQL Workbench, go to 'Server' and click on 'Data Import'
- Choose option "Import from Self-Contained File" and pick the sql file 'pokedexMySQLdump.sql', you not would 
need to choose a 'Default Target Schema' because in the dump file will create the database schema called "pokdex_project"
- Refresh the schemas and the user will see that 'pokedex_project' schema will be imported with all the data 
from the csv files
- Run main.py in Pycharm

Running the main.py will create a program that allows the user to input and receive information about the 
Pokemon containing the information gained from the database.

I used the 'Table Data Import Wizard' built in MySQL Workbench to import the data from the .csv files
so all the data should be in the dump. If not, the CSV folder will have all the required table data to be 
imported to be wizard in MySQL Workbench
