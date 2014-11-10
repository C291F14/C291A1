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
				eNo = str(input("Please enter employee number of doctor, or B to return: ")).strip().lower()
				if eNo == "b":
					curs.close()
					return
				else:
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




