# Patient Information Update written by Cody Ingram
import cx_Oracle as cx
import sys

def testChange(con, HCno):
	# change allowed tests
	while True:
		opt = str(input("Please select an option:\n 1 - Restrict test\n 2 - Unrestrict test\n 3 - Back"))

		if opt == "1":
			#add a new dissallowed test

			while True:
				print()

				typeid = int(input("Please enter type id of test to restrict:\n"))

				curs = con.cursor()
				query = """INSERT INTO not_allowed VALUES (:HC, :id)"""

				try:
					curs.execute(query, {'HC': HCno, 'id': typeid})
					con.commit()
					curs.close()
					break
				except cx.DatabaseError as exc:
					error, = exc.args
					print( sys.stderr, "Oracle code:", error.code)
					print( sys.stderr, "Oracle message:", error.message)
					print("Ensure that the test id is valid and restriction doesn't already exist")
					curs.close()
					break

		elif opt == "2":
			#delete a test from dissalowed tests. print out tests, select which to delete
			while True:
				print()

				curs = con.cursor()
				query = """SELECT type_id FROM not_allowed WHERE health_care_no = :HC"""
				try:
					curs.execute(query, {'HC': HCno})
				except cx.DatabaseError as exc:
					error, = exc.args
					print( sys.stderr, "Oracle code:", error.code)
					print( sys.stderr, "Oracle message:", error.message)
					break

				rows = curs.fetchall()
				if len(rows) < 1:
					print("No restricted tests for patient " + str(HCno) + "please try again") 
					break

				print("Restricted tests for patient " + str(HCno) + ":")
				myRow = []
				for row in rows:
					print(row[0])
					myRow.append(row[0])

				delete = input("Please enter type id of the test you wish to unrestrict: ")
				try:
					int(delete)
				except:
					print("Input Error, please try again")
					break

				if delete not in myRow:
					print("Test not currently restricted")
					break
						
				query = """DELETE FROM not_allowed WHERE health_care_no = :HC and type_id = :id"""

				try:
					curs.execute(query, {'HC': HCno, 'id': delete})
					con.commit()
					curs.close()
					break
				except cx.DatabaseError as exc:
					error, = exc.args
					print( sys.stderr, "Oracle code:", error.code)
					print( sys.stderr, "Oracle message:", error.message)
					break

		elif opt == "3":
			if curs:
				curs.close()
			return
		else:
			print("Invalid input, please try again")

def updatePatient(con):
	# get all info then select update
	curs = con.cursor()

	while True:
		print()
		HCno = str(input("Please enter healthcare number of the patient you wish to update, or B to return: ")).strip().lower()
		if HCno == "b":
			curs.close()
			return
		else:
			#check existence of HCno
			HCno = int(HCno)
			query = """SELECT * from patient where health_care_no = :HC"""
			try:
				curs.execute(query, {'HC': HCno})
			except cx.DatabaseError as exc:
				error, = exc.args
				print( sys.stderr, "Oracle code:", error.code)
				print( sys.stderr, "Oracle message:", error.message)
				curs.close()
				return

			rows = curs.fetchall()
			if len(rows) < 1:
				print("Patient doesn't exists, please try again")
				continue

			while True:
				print()
				updateSelect = str(input("Please select which attributes you want to update for " + str(HCno) + "\n 1 - Name\n 2 - Address\n 3 - Birthday\n 4 - Phone #\n 5 - Allowed Tests\n 6 - Back\n"))

				# update name
				if updateSelect == "1":
					pname = str(input("Enter name: ")).strip()

					if len(pname) > 100:
						print("Name too long, Name not updated")
					else:
						update = """UPDATE patient SET name = :myname WHERE health_care_no = :pHCno"""

						try:
							curs.execute(update, {'myname': pname, 'pHCno': HCno})
							con.commit()
						except cx.DatabaseError as exc:
							error, = exc.args
							print( sys.stderr, "Oracle code:", error.code)
							print( sys.stderr, "Oracle message:", error.message)
							print("Error, patient not updated")

				# update address
				elif updateSelect == "2":
					paddress = str(input("Enter address: ")).strip()

					if len(paddress) > 200:
						print("Adress too long, Address not updated")
					else:
						update = """UPDATE patient SET address = :myaddress WHERE health_care_no = :pHCno"""

						try:
							curs.execute(update, {'myaddress': paddress, 'pHCno': HCno})
							con.commit()
						except cx.DatabaseError as exc:
							error, = exc.args
							print( sys.stderr, "Oracle code:", error.code)
							print( sys.stderr, "Oracle message:", error.message)
							print("Error, patient not updated")

				# update birthday
				elif updateSelect == "3":
					pbirthday = str(input("Enter birthday (YYYY-MM-DD): ")).strip()

					if len(pbirthday) != 10:
						print("Invalid date, birthday not updated")
					else:
						update = """UPDATE patient SET birth_day = TO_DATE(:mybirthday, 'YYYY-MM-DD') WHERE health_care_no = :pHCno"""

						try:
							curs.execute(update, {'mybirthday': pbirthday, 'pHCno': HCno})
							con.commit()
						except cx.DatabaseError as exc:
							error, = exc.args
							print( sys.stderr, "Oracle code:", error.code)
							print( sys.stderr, "Oracle message:", error.message)
							print("Error, patient not updated\nEnsure date formatting is correct")

				# update phone
				elif updateSelect == "4":
					pphoneNum = str(input("Enter 10 digit phone number: ")).strip()

					if len(pphoneNum) != 10:
						print("Invalid phone number, Phone number not updated")
					else:
						update = """UPDATE patient SET phone = :myphone where health_care_no = :pHCno"""

						try:
							curs.execute(update, {'myphone': pphoneNum, 'pHCno': HCno})
							con.commit()
						except cx.DatabaseError as exc:
							error, = exc.args
							print( sys.stderr, "Oracle code:", error.code)
							print( sys.stderr, "Oracle message:", error.message)
							print("Error, patient not updated")

				# change tests 
				elif updateSelect == "5":
					testChange(con, HCno)

				# back to menu
				elif updateSelect == "6":
					break

				# error
				else:
					print("Invalid input")



def addPatient(con):

	curs = con.cursor()

	while True:
		print()
		HCno = str(input("Please enter healthcare #, or B to return: ")).strip().lower()
		if HCno == "b":
			curs.close()
			return
		else:
			#check existence of HCno
			HCno = int(HCno)
			query = """SELECT * from patient where health_care_no = :HC"""
			try:
				curs.execute(query, {'HC': HCno})
			except cx.DatabaseError as exc:
				error, = exc.args
				print( sys.stderr, "Oracle code:", error.code)
				print( sys.stderr, "Oracle message:", error.message)
				curs.close()
				return

			rows = curs.fetchall()
			if len(rows) > 0:
				print("Patient already exists, please try again")
				continue

			name = str(input("Please enter name, or B to return: ")).strip()
			if name == "b" or name == "B":
				curs.close()
				return
			else:

				query = """INSERT INTO patient(health_care_no, name) VALUES (:hc, :name)"""

				try:
					curs.execute(query, {'hc': HCno, 'name': name})
					con.commit()
					print("Patient created")
				except cx.DatabaseError as exc:
					error, = exc.args
					print( sys.stderr, "Oracle code:", error.code)
					print( sys.stderr, "Oracle message:", error.message)
					print("Error, patient not added")
					continue

				a = input("Press 1 to finish, Press 2 to update")
				if a == "1":
					continue
				elif a == "2":
					updatePatient(con)
				else:
					print("Invalid Input")

def updateInfo(con):

	while True:

		print()
		menuChoice = str(input("Please select an option:\n 1 - Update Existing Patient\n 2 - Add New Patient\n 3 - Exit To Main Menu\n")).strip()

		if menuChoice == "1":
			updatePatient(con)
		elif menuChoice == "2":
			addPatient(con)
		elif menuChoice == "3":
			return
		else:
			print("Invalid input, please try again")
