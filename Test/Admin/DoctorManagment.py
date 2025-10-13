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















def update_info():
    print("update info")

def view_doctor():
    print("list of all Doctors Available")
    ViewDoctor_Query = "SELECT * FROM DOCTORS"
    mycursor.execute(ViewDoctor_Query)
    doctor = mycursor.fetchall()

    headers = ["fullname","specialization","contact","available_days","consultation_fee"]
    print(tabulate(doctor,headers=headers,tablefmt="fancy_grid"))




def delete_doctor():
    print("delete a doctor") 