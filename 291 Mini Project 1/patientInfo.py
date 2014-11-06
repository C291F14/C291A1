# Patient Information Update written by Cody Ingram

def updatePatient(con):
	# get all info then select update
	curs = con.cursor()

	while True:
		HCno = str(input("Please enter healthcare number of the patient you wish to update, or B to return: ")).strip().lowercase()
		if HCno == "b":
			curs.close()
			return
		else:
			#check existence of HCno
			int(HCno)

			try:
				curs.execute("SELECT * FROM patient WHERE health_care_no = %f" % (HCno))
			except cx.DatabaseError as exc:
				error = exc.args
				print( sys.stderr, "Oracle code:", error.code)
				print( sys.stderr, "Oracle message:", error.message)
				curs.close()
				return

			rows = curs.fetchall()
			if len(rows) < 1:
				print("Patient doesn't exists, please try again")
				continue

			while True:
				updateSelect = str(input("Please select which attributes you want to update for " + str(HCno) + "\n 1 - Name\n 2 - Address\n 3 - Birthday\n 4 - Phone #\n 6 - Back\n"))

				# update name
				if updateSelect == "1":
					pname = str(input("Enter name: ")).strip()

					if len(pname) > 100:
						print("Name too long, Name not updated")
					else:
						update = """update patient(health_care_no, name, address, birthday, phone) set name = :name where health_care_no = :pHCno"""

						try:
							curs.execute(update, {'name': pname, 'pHCno': HCno})
							con.commit()
						except cx.DatabaseError as exc:
							error = exc.args
							print( sys.stderr, "Oracle code:", error.code)
							print( sys.stderr, "Oracle message:", error.message)
							print("Error, patient not updated")

				# update address
				elif updateSelect == "2":
					paddress = str(input("Enter address: ")).strip()

					if len(paddress) > 200:
						print("Adress too long, Address not updated")
					else:
						update = """update patient(health_care_no, name, address, birthday, phone) set address = :address where health_care_no = :pHCno"""

						try:
							curs.execute(update, {'address': paddress, 'pHCno': HCno})
							con.commit()
						except cx.DatabaseError as exc:
							error = exc.args
							print( sys.stderr, "Oracle code:", error.code)
							print( sys.stderr, "Oracle message:", error.message)
							print("Error, patient not updated")

				# update birthday
				elif updateSelect == "3":
					pbirthday = str(input("Enter birthday (YYYY-MM-DD): ")).strip()

					if len(birthday) != 10:
						print("Invalid date, birthday not updated")
					else:
						update = """update patient(health_care_no, name, address, birthday, phone) set birthday = TO_DATE(:birthday, 'YYYY-MM-DD') where health_care_no = :pHCno"""

						try:
							curs.execute(update, {'birthday': pbirthday, 'pHCno': HCno})
							con.commit()
						except cx.DatabaseError as exc:
							error = exc.args
							print( sys.stderr, "Oracle code:", error.code)
							print( sys.stderr, "Oracle message:", error.message)
							print("Error, patient not updated\nEnsure date formatting is correct")

				# update phone
				elif updateSelect == "4":
					pphoneNum = str(input("Enter 10 digit phone number: ")).strip()

					if len(pphoneNum) != 10:
						print("Invalid phone number, Phone number not updated")
					else:
						update = """update patient(health_care_no, name, address, birthday, phone) set phone = :phone where health_care_no = :pHCno"""

						try:
							curs.execute(update, {'phone': pphoneNum, 'pHCno': HCno})
							con.commit()
						except cx.DatabaseError as exc:
							error = exc.args
							print( sys.stderr, "Oracle code:", error.code)
							print( sys.stderr, "Oracle message:", error.message)
							print("Error, patient not updated")


				# back to menu
				elif updateSelect == "6":
					break

				# error
				else:
					print("Invalid input")



def addPatient(con):
	print("nope")
	return

def updateInfo(con):

	while True:

		menuChoice = str(input("Please select an option:\n 1 - Update Existing Patient\n 2 - Add New Patient\n 3 - Exit To Main Menu\n")).strip()

		if menuChoice == "1":
			updatePatient(con)
		elif menuChoice == "2":
			addPatient(con)
		elif menuChoice == "3":
			return
		else:
			print("Invalid input, please try again")
