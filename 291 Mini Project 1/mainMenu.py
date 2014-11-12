import sys
import cx_Oracle as cx
from getpass import *
from patientInfo import * 
from searchEngine import *

# Main menu for healthcare database written by Cody Ingram

def dbInfo():
	
	# User imputs Oracle username/password
	dbusr = str(input("Please input Oracle db username: ")).strip()
	if not user:
    	user=getpass.getuser()
	dbpass = getpass()
	
	# create a string for database connection
	constr = str(dbusr + "/" + dbpass + "@gwynne.cs.ualberta.ca:1521/CRS")	
	
	return constr

def menuOption():
	
	# choose menu option
	menuChoice = str(input("Please Select An Option:\n 1 - Perscription\n 2 - Medical Test\n 3 - Patient Information Update\n 4 - Search Engine\n 5 - Exit\n"))
	
	if menuChoice == "1":
		print("# call perscription")
		return True
	elif menuChoice == "2":
		print("# call Medical Test")
		return True
	elif menuChoice == "3":
		updateInfo(con) #updatePatientInfo
		return True
	elif menuChoice == "4":
		print("# call search engine")
		return True
	elif menuChoice == "5":
		con.close()
		sys.exit()
	else:
		return False
	
def main():

	# Give database info and try connection. If failure, report
	# error and give the option to exit or try again
	while True:
		constr = dbInfo()
	
		try:
			con = cx.connect(constr)
			break
		
		except cx.DatabaseError as exc:
			error, = exc.args
			print( sys.stderr, "Oracle code:", error.code)
			print( sys.stderr, "Oracle message:", error.message)
			
			while True:
				opt = input("Press 1 to try again, press 2 to exit\n")
				if opt == "1":
					break
				elif opt == "2":
					con.close()
					sys.exit()
				else:
					Print("Invalid input")
			
	# main menu starts, give options for applications	
	print("Welcome to the best database application ever!")
	
	while True:
		opt2 = menuOption()
		while opt2 == False:
			print("Invalid Input")
			opt2 = menuOption()

main()