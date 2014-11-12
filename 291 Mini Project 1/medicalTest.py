# medical test written by Cody Ingram
import cx_Oracle as cx
import sys

# default option of current date
# give options of can_conduct for tests

def testResult(con):

	curs = con.cursor()

	while True:
		print()
		HCno = str(input("Please enter healthcare number of the patient, or B to return: ")).strip().lower()
		if HCno == "b":
			curs.close()
			return
		else:
			#check existence of HCno
			try: 
				int(HCno)
			except:
				print("Invalid healthcare #, please try again")
				continue

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
				docName = str(input("Please enter name of doctor, or B to return: ")).strip()
				if docName == "b":
					curs.close()
					return
				else:
					# get doc eNo from name
					query = """SELECT doctor.employee_no FROM patient, doctor WHERE doctor.health_care_no = patient.health_care_no AND patient.name = :name"""

					try:
						curs.execute(query, {'name': docName})
					except cx.DatabaseError as exc:
						error, = exc.args
						print( sys.stderr, "Oracle code:", error.code)
						print( sys.stderr, "Oracle message:", error.message)
						curs.close()
						return

					rows = curs.fetchall()
					if len(rows) < 1:
						print("Doctor doesnt exist, please try again")
						continue

					eNo = rows[0][0]

					try:
						int(eNo)
					except:
						print("Invalid employee #, please try again")
						continue

					query = """SELECT * from doctor where employee_no = :EN"""
					try:
						curs.execute(query, {'EN': eNo})
					except cx.DatabaseError as exc:
						error, = exc.args
						print( sys.stderr, "Oracle code:", error.code)
						print( sys.stderr, "Oracle message:", error.message)
						curs.close()
						return

					rows = curs.fetchall()
					if len(rows) < 1:
						print("Doctor doesn't exists, please try again")
						continue

					query = """SELECT * FROM test_record WHERE patient_no = :HC AND employee_no = :EN"""
					try:
						curs.execute(query, {'HC': HCno, 'EN': eNo})
					except cx.DatabaseError as exc:
						error, = exc.args
						print( sys.stderr, "Oracle code:", error.code)
						print( sys.stderr, "Oracle message:", error.message)
						curs.close()
						return

					rows = curs.fetchall()
					if len(rows) < 1:
						print("No perscription exists for this test, request rejected")
						curs.close()
						return

					while True:

						query = """SELECT test_id FROM test_record WHERE patient_no = :pno AND employee_no = :eno"""
						try:
							curs.execute(query, {'pno': HCno, 'eno': eNo})
						except cx.DatabaseError as exc:
							error, = exc.args
							print( sys.stderr, "Oracle code:", error.code)
							print( sys.stderr, "Oracle message:", error.message)
							curs.close()
							return

						rows = curs.fetchall()
						for row in rows:
							print("Test ID's Prescribed by " + docName + "to" + str(HCno) + ":")
							print(row[0])

						test_id = input("Please enter test id of the test you wish to update, or B to exit: ").strip().lower()
						if test_id == "b":
							curs.close()
							return
						try:
							int(test_id)
						except:
							print("Invalid ID")
							continue

						while True:

							opt = input("Please select an option:\n 1 - Update Lab Name\n 2 - Update Test Date\n 3 - Update Test Result\n 4 - Back\n")

							if opt == "1":
								#update lab name
								lab_name = input("Please enter lab name: ")
								if len(lab_name) > 25:
									print("Invalid lab name, test not updated")
									continue

								query = """UPDATE test_record SET medical_lab = :name WHERE patient_no = :pno AND employee_no = :eno AND test_id = :tid"""

								try:
									curs.execute(query, {'name': lab_name, 'pno': HCno, 'eno': eNo, 'tid': test_id})
									con.commit()
								except cx.DatabaseError as exc:
									error, = exc.args
									print( sys.stderr, "Oracle code:", error.code)
									print( sys.stderr, "Oracle message:", error.message)
									print("Error, test not updated")

							elif opt == "2":
								#update test date 
								mydate = input("Please enter test date (YYYY-MM-DD): ").strip()
								if len(mydate) != 10:
									print("Invalid date, test not updated")
								else:

									query = """UPDATE test_record SET test_date = TO_DATE(:dates, 'YYYY-MM-DD') WHERE patient_no = :pno AND employee_no = :eno AND test_id = :tid"""

									try:
										curs.execute(query, {'dates': mydate, 'pno': HCno, 'eno': eNo, 'tid': test_id})
										con.commit()
									except cx.DatabaseError as exc:
										error, = exc.args
										print( sys.stderr, "Oracle code:", error.code)
										print( sys.stderr, "Oracle message:", error.message)
										print("Error, test not updated")

							elif opt == "3":
								#update test result
								result = input("Please enter test results: ").strip()

								if len(result) > 1024:
									print("Results too long, test not updated")
								else:
									query = """UPDATE test_record SET result = :res WHERE patient_no = :pno AND employee_no = :eno AND test_id = :tid"""

									try:
										curs.execute(query, {'res': result, 'pno': HCno, 'eno': eNo, 'tid': test_id})
										con.commit()
									except cx.DatabaseError as exc:
										error, = exc.args
										print( sys.stderr, "Oracle code:", error.code)
										print( sys.stderr, "Oracle message:", error.message)
										print("Error, test not updated")

							elif opt == "4":
								break
							else:
								print("Invalid input, please try again")
								continue




