import pymysql
from DoctorManagment import add_doctors,update_info,view_doctor,delete_doctor
mydb = pymysql.connect(
    host="localhost",
    port=3307,
    user="Admin",
    password="myAdmin",
    database="hospitalDB" 
)

mycursor = mydb.cursor()
print("connected succfully")
def doctor_managment():
    while True:
        print("\n===== Doctor Management =====")
        print("1. Add new doctors")
        print("2. Update doctor info")
        print("3. View all doctors")
        print("4. Delete a doctor")
        print("5. exit")

        choice = input("select an option: ")

        if choice == "1":
            add_doctors()
        elif choice == "2":
            update_info()
        elif choice == "3":
            view_doctor()
        elif choice == "4":
            delete_doctor()
        elif choice == "5":
            break
        else:
            print("invalid choice , try again")

def mainMenu():
    while True:
        print("================welcome to TOP CARE HOSPITAL MANAGMENTS SYSTEM===============")
        print("\n===== ADMIN DASHBOARD =====")
        print("1. Manage Doctors")
        print("3. View Patients")
        print("4. Monitor Appointments")
        print("5. Reports & Analytics")
        print("6. Logout")

        choice = input("select an option: ")

        if choice == "1":
            doctor_managment()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            break
        else:
            print("invalid choice , try again")
mainMenu()

