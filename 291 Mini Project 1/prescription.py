# C291 Project 1
# Prescription
# Chris Li

#**************************************************************************************************************

# This application program is used by a doctor to "prescribe a medical test to a patient."
# The program shall "allow a user to enter the detailed information about the prescription, 
# including the employee_no or name of the doctor who prescribes the test, the test name, 
# and the name and/or the health_care_no of the patient." As expected, all the prescriptions 
# conflict to the not_allowed constraints must be rejected.

# Your program shall automatically generate a suitable test_id for the test_record, and use 
# the NULL value properly for the task.

# One needs not to specify when and where the test shall be conducted.

#**************************************************************************************************************

# Prescription format? Goes in mainMenu.py? Do we need this at all?
#**************************************************************************************************************
#class Prescription:
    
#    def __init__(self, iemployee_no, idoctor_name, itest_name, ihealth_care_no, ipatient_name, itest_id):
#        self.employee_no = iemployee_no
#        self.doctor_name = idoctor_name
#        self.test_name = itest_name
#        self.health_care_no = ihealth_care_no
#        self.patient_name = ipatient_name
#        self.test_id = itest_id
#**************************************************************************************************************

import sys
import cx_Oracle as cx
import time

# May have to exit multiple times before getting about to desired Menu.

# Called to add more input to prescription if a valid doctor employee_no/doctor_name exists
def more_input(con, EmployeeNumber):

    confirm = set(['yes'])

    ###
    curs1 = con.cursor()
    curs2 = con.cursor()

    try:
        ans = 'yes'

        # User can reattempt to create prescription if previously failed
        while ans in confirm:

            P1menuChoice = str(input("Okay, Please Select A Creation Option:\n 1 - Create Prescription\n 2 - Exit To Validation Menu\n"))

            if P1menuChoice == "1":

                print("Please Enter the Following Details About the Prescription.\n")
                
                try:
                    TestName = input("Enter the Exact Test Name: ")
                    HealthCareNumber = int(input("Enter 'Patient' Health Care Number: "))

                except:
                    print("Invalid Input!\n")

                try:
                    # Check if Patient is able to take the test prescribed.

                    # Retrieve the type_id for the TestName given.
                    curs1.execute("""SELECT type_id FROM test_type WHERE test_name = :tname""", {'tname':TestName})
                    # rows1 = (type_id)
                    rows1 = curs1.fetchone()

                    if rows1 == None:
                        print("No Test Found in Database!\n")
                    else:

                        try:
                            NotAllowedCheck = (HealthCareNumber, rows1)

                            curs2.execute("""SELECT * FROM not_allowed""")
                            # rows2 = [(health_care_no, type_id), (health_care_no, type_id), (health_care_no, type_id), ...]
                            rows2 = curs2.fetchall()

                            if NotAllowedCheck in rows2:
                                print("Not Allowed to Take Test!\n")
                            else:
                                print("Allowed to Take Test!\n")
                                insert_row(rows1, EmployeeNumber, HealthCareNumber, con);
                                #break

                        except cx.DatabaseError as exc:
                            error, = exc.args
                            print( sys.stderr, "Oracle code:", error.code)
                            print( sys.stderr, "Oracle message:", error.message)
                            print("Error, could not access data\n")
                        
     #                   else: 
      #                      if NotAllowedCheck in rows2:
       #                         print("Not Allowed to Take Test!\n")
        #                    else:
         #                       print("Allowed to Take Test!\n")
          #                      insert_row(rows1, EmployeeNumber, HealthCareNumber, con);
                                #break

                except cx.DatabaseError as exc:
                    error, = exc.args
                    print( sys.stderr, "Oracle code:", error.code)
                    print( sys.stderr, "Oracle message:", error.message)
                    print("Error, Could not access database\n")

            elif P1menuChoice == "2":
                curs1.close()
                curs2.close()
                cursSeq.close()
                #connection.close()
                #sys.exit()
                return

            else:
                print("Please Select a Number From 1 to 2!\n")

    except:
        print("See You Next Time!\n")


# test_record(test_id,type_id,patient_no,employee_no,medical_lab,result,prescribe_date,test_date)
# Called to insert a row of information into 'test_record' table
def insert_row(TypeId, EmployeeNumber, HealthCareNumber, con):

    # Getting the prescription date and converting it to be read by SQL.
    PrescribeDate = time.strftime("%Y/%m/%d")

    print("inserting row")

    # Create sequence to generate unique 'test_id'
    cursSeq = con.cursor()
    createSeqStr = "CREATE SEQUENCE test_id_seq INCREMENT BY 1 START WITH 100000"
    cursSeq.execute(createSeqStr)
        
    #Creating and setting cursor for insert statement
    cursInsert = con.cursor()
    cursInsert.bindarraysize = 8

    #Inserting new row into 'test_record' table
    insert = """insert into test_record values (:test_id, :type_id, :patient_no, :employee_no, :medical_lab, :result, TO_DATE(:prescribe_date, 'YYYY/MM/DD'), :test_date)"""
    try:
        cursInsert.execute(insert,{'test_id':test_id_seq.NEXTVAL, 'type_id':TypeId, 'patient_no':HealthCareNumber, 'employee_no':EmployeeNumber, 'medical_lab':NULL, 'result':NULL, 'prescribe_date':PrescribeDate, 'test_date':NULL})
        con.commit()
        print("New Prescription Record Added!\n")
        return

    except cx.DatabaseError as exc:
        error, = exc.args
        print( sys.stderr, "Oracle code:", error.code)
        print( sys.stderr, "Oracle message:", error.message)
        print("Error, There was a problem putting your prescription into the database!\n")
        return

#    else:
        
        


#        P2menuChoice = str(input("Please Select An Option:\n 1 - Create Another Prescription\n 2 - Exit To Creation Menu\n"))

#        if P2menuChoice == "1":
#            more_input();

#        elif P2menuChoice == "2":
#            print("Goodbye!\n")
#            curs1.close()
#            curs2.close()
#            cursSeq.close()
#            cursInsert.close()
            #connection.close()
            #sys.exit()
#            return


# Used by a doctor to prescribe a medical test to a patient
def prescription(con):

    #cnstr = str(dbusr + "/" + dbpass + "@gwynne.cs.ualberta.ca:1521:CRS")
    
    confirm = set(['yes'])

    try:
        #connection = cx.connect(constr)
        
        curs = con.cursor()
        ans = 'yes'
        
        # User can reattempt to create a prescription again if previously failed
        while ans in confirm:
            
            PmenuChoice = str(input("Hello Doctor, Please Select a Validation Option:\n 1 - Validate Employee Number\n 2 - Validate Doctor Name\n 3 - Exit to Main Menu\n"))
            
            if PmenuChoice == "1":
                try:
                    employee_no = input("Enter Your EMPLOYEE_NO: ")
                
                    # check if employee_no of doctor exists in 'doctor' table.
                    curs.execute("SELECT employee_no FROM doctor;")
                    rows = curs.fetchall()
                    if employee_no not in rows:
                        print("> EMPLOYEE_NO entered does not exist!\n")
                    else:
                        more_input(con, employee_no);
                        #break

                except cx.DatabaseError as exc:
                    error, = exc.args
                    print( sys.stderr, "Oracle code:", error.code)
                    print( sys.stderr, "Oracle message:", error.message)
                    print("Error, Could not find employee number\n")

            elif PmenuChoice == "2":
                try:
                    doctor_name = input("Enter your first and last name. Format => 'John Doe': ")
		    
                    # check if doctor_name is a exists in 'doctor' table by comparing the health_care_no in both the 'patient' and 'doctor' table.
                    curs.execute("""SELECT d.employee_no FROM patient p, doctor d WHERE p.health_care_no = d.health_care_no AND p.name = :name""", {'name':doctor_name})
                    rows = curs.fetchall()
                    if len(rows) < 1:
                        print("> Doctor does not exist or you are only a patient!\n")
                    else:
                        more_input(con, rows[0][0]);
                        #break

                except cx.DatabaseError as exc:
                    error, = exc.args
                    print( sys.stderr, "Oracle code:", error.code)
                    print( sys.stderr, "Oracle message:", error.message)
                    print("Error, Could not find doctor name\n")
	
            elif PmenuChoice == "3":
                curs.close()
                #connection.close()
                #sys.exit()
                return

            else:
                print("> Please Select a Number from 1 to 3!\n")

    except:
        print("\n")



