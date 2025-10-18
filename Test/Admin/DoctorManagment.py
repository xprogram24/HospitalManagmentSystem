import pymysql
from tabulate import tabulate
mydb = pymysql.connect(
    host="localhost",
    port=3307,
    user="Admin",
    password="myAdmin",
    database="hospitalDB" 
)

mycursor = mydb.cursor()
print("connected succfully")


'''
Add new doctors

Update doctor info (department, fee, availability)

View all doctors

Delete a doctor'''

def add_doctors():
    print("add a doctor")

    addDoctoR_Query = "INSERT INTO DOCTORS (fullname,specialization,contact,available_days,consultation_fee) VALUES (%s,%s,%s,%s,%s)"
    fullname = input("please input doctor name: ").strip().lower()
    specialization = input("please input doctor specilization: ").strip().lower()
    contact = input("please input doctor contact: ").strip().lower()
    available_Days = input("please input Available days: ").strip().lower()
    consultation_fee = input("please enter consultation_fee: ").strip().lower()
    mycursor.execute(addDoctoR_Query,(fullname,specialization,contact,available_Days,consultation_fee))
    mydb.commit()
    print(mycursor.rowcount,"record added")


def view_doctor():
    print("list of all Doctors Available")
    ViewDoctor_Query = "SELECT * FROM DOCTORS"
    mycursor.execute(ViewDoctor_Query)
    doctor = mycursor.fetchall()

    headers = ["fullname","specialization","contact","available_days","consultation_fee","Doctor_no"]
    print(tabulate(doctor,headers=headers,tablefmt="fancy_grid"))





def update_info():
    view_doctor()
    doc_no = input("Enter Doctors_NO: ").strip()
    while True:
        print("what would you like to change")
        print("OPTION: ")
        print("1. Fullname (with Dr)")
        print("2. Specialization")
        print("3. contact")
        print("4. available days")
        print("5. consultation_fee")
        print("6. Doc_No")
        print("7. Exit")

        option = input("select an option: ")
        if option == "1":
            new_data = input("input new Fullname: ")
            updateQuery = "UPDATE Doctors SET fullname = %s WHERE doc_no = %s"
            mycursor.execute(updateQuery,(new_data,doc_no))
            mydb.commit()
            print("successfully updated")

        elif option == "2":
            new_data = input("input new specialization: ")
            updateQuery = "UPDATE Doctors SET specialization = %s WHERE doc_no = %s"
            mycursor.execute(updateQuery,(new_data,doc_no))
            mydb.commit()
            print("successfully updated")

        elif option == "3":
            new_data = input("input new contact: ")
            updateQuery = "UPDATE Doctors SET contact = %s WHERE doc_no = %s"
            mycursor.execute(updateQuery,(new_data,doc_no))
            mydb.commit()
            print("successfully updated")

        elif option == "4":
            new_data = input("input new available_days: ")
            updateQuery = "UPDATE Doctors SET available_days = %s WHERE doc_no = %s"
            mycursor.execute(updateQuery,(new_data,doc_no))
            mydb.commit()
            print("successfully updated")

        elif option == "5":
            new_data = input("input new consultation_fee: ")
            updateQuery = "UPDATE Doctors SET consultation_fee = %s WHERE doc_no = %s"
            mycursor.execute(updateQuery,(new_data,doc_no))
            mydb.commit()
            print("successfully updated")

        elif option == "6":
            new_data = input("input new doc_no: ")
            updateQuery = "UPDATE Doctors SET doc_no = %s WHERE doc_no = %s"
            mycursor.execute(updateQuery,(new_data,doc_no))
            mydb.commit()
            print("successfully updated")
        elif option == "7":
            break
        else:
            print("invalid")
update_info()


def view_doctor():
    print("list of all Doctors Available")
    ViewDoctor_Query = "SELECT * FROM DOCTORS"
    mycursor.execute(ViewDoctor_Query)
    doctor = mycursor.fetchall()

    headers = ["fullname","specialization","contact","available_days","consultation_fee","Doctor_no"]
    print(tabulate(doctor,headers=headers,tablefmt="fancy_grid"))




def delete_doctor():
    print("--------Delete doctors---------")
    view_doctor()
    doc_no = input("Enter your doctor number")
    delete_query = "DELETE  FROM doctors WHERE doc_no = %s "
    mycursor.execute(delete_query,(doc_no))
    mydb.commit()
    print("delete sucessful ✅")

#fill data

def add_query():
   
    add = "INSERT INTO Doctors (fullname, specialization, contact, available_days, consultation_fee,doc_no) VALUES (%s,%s,%s,%s,%s,%s)"
    value = [
         ("Dr. James Okoro", "Cardiologist", "08124567890", "Monday–Friday", "25000","CA11"),
        ("Dr. Sarah Bello", "Dermatologist", "08135678901", "Tuesday–Saturday", "18000","DM11"),
        ("Dr. Tunde Afolabi", "Neurologist", "08099887766", "Monday–Thursday", "30000","NE11"),
        ("Dr. Chinyere Eze", "Pediatrician", "08123456789", "Monday–Friday", "15000","PD10"),
        ("Dr. Kelvin Adeyemi", "Orthopedic Surgeon", "09087654321", "Wednesday–Saturday", "28000","OS21"),
        ("Dr. Linda Ogbonna", "Gynecologist", "08034567812", "Monday–Friday", "22000","GY12"),
        ("Dr. Yusuf Garba", "Ophthalmologist", "08198765432", "Tuesday–Friday", "20000","OP11"),
        ("Dr. Funke Ajayi", "ENT Specialist", "09023456781", "Monday–Thursday", "17000","ENT55"),
        ("Dr. Patrick Nwosu", "General Practitioner", "08067891234", "Monday–Sunday", "12000","GP12"),
        ("Dr. Victoria Johnson", "Psychiatrist", "08122334455", "Wednesday–Saturday", "24000","PSY11")


    ]

    mycursor.executemany(add,value)
    mydb.commit()
    print("added")
