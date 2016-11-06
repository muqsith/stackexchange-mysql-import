# stackexchange-mysql-import
Python script to import stack exchange site dump into MySQL.

This script was written/tested/used on Ubuntu 16.04 (never tested on windows)

Please install 7zip, if it is not installed.

`$ sudo apt install p7zip-full`

Steps to import stack exchange site data into MySQL

Assuming you have site dump like askubuntu.com.7z

* In your MySQL, create database with desired name using TableCreationQueries.sql script (here i have created a database with name 'askubuntu'). 
	* a. Edit TableCreationQueries.sql script and change database name with the one you want.
	* b. start mysql client and type below command.
	
		`
		mysql> source /path/to/TableCreationQueries.sql
		`
		
* Edit mysql-connector.cnf, enter your MySQL's user, password and the database created in step 1.
* Opten terminal and execute the script

	
	`
	$ ./script.py /path/to/askubuntu.com.7z
	`
	
	`
	(or)
	`
	
	`
	$ python3.5 script.py /path/to/askubuntu.com.7z
	`

*Optional steps*

* If you have already extracted the 7z compressed files then you can point the folder in the script instead of compressed file.

	`
	$ ./script.py /path/to/folder-with-xmls
	`
	
There is also a simple (better) way to import using Ruby, follow link.
	https://gist.github.com/gousiosg/7600626
		