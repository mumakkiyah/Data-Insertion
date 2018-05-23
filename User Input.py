import mysql.connector
from mysql.connector import Error, MySQLConnection
import time 

dbconfig = {
	'host': 'localhost',
	'database': 'employee_db',
	'user': 'mustafa',
	'password': 'Passw0rd'
	}


try: 
	cnx = MySQLConnection(**dbconfig)
	cursor = cnx.cursor()

	if cnx.is_connected():
		print('Connected to the database')
except Error as e:
	print(e)

time.sleep(2)

#Data Insertion
def user_input():
	emp_fname = input("what is the employee first name: ")
	emp_lname = input("what is the employee last name: ")
	emp_dob = input("what is the employee date of birth: ")
	emp_city = input("where does the employee live: ")

	print('inserting values into the table ....')

	time.sleep(5)

	cursor.execute("""INSERT INTO emp_info (Emp_FName,Emp_LName,Emp_DOB,Emp_City) VALUES (%s, %s, %s, %s)""", 
	(emp_fname, emp_lname, emp_dob, emp_city))

if __name__ == "__main__":
	user_input()

#Query the database
def query_all():
	print("Fetching all results from the table ....")
	time.sleep(5)
	cursor.execute("SELECT * FROM emp_info")
	rows = cursor.fetchall()
	
	for row in rows:
		print(row)
		
if __name__ == "__main__":
	query_all()


cnx.commit()
cnx.close()

	