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


'''add patients ,delete patinent,update patinets,view patients'''

'''
fullname VARCHAR(255),
	dateof_birth DATE,
	gender VARCHAR(10),
	contact VARCHAR(50),
	address TEXT,
	date_registered DATETIME,
	cardnumber TEXT NULL
'''

def fill_patient():
    addQuery = "INSERT INTO patients (fullname,dateof_birth,gender,contact,address,date_registered,cardnumber) VALUE(%s,%s,%s,%s,%s,%s,%s)"
    value = [
        ('David Johnson', '1997-04-21', 'Male', '+2348061234567', '10 Ahmadu Bello Way, Kaduna', '2025-10-01 09:45:00', 'CARD2019483'),
        ('Amaka Obi', '2001-02-13', 'Female', '+2348156789023', '3 Okpara Avenue, Enugu', '2025-10-02 13:15:00','CARD48739' ),
        ('Samuel Okorie', '1996-09-05', 'Male', '+2348089123456', '22 Herbert Macaulay Road, Yaba, Lagos', '2025-10-03 08:30:00', 'CARD4873920'),
        ('Janet Musa', '1999-11-11', 'Female', '+2348072345678', '18 Aliyu Street, Garki, Abuja', '2025-10-03 17:10:00','CARD40000'),
        ('Kingsley Nnaji', '1998-06-28', 'Male', '+2349053456781', '5 Iweka Road, Onitsha', '2025-10-04 15:45:00', 'CARD3920471'),
        ('Zainab Abdullahi', '2000-12-20', 'Female', '+2348095672314', '11 Zaria Road, Kano', '2025-10-04 10:20:00','CARD487777'),
        ('Peter Chukwu', '1995-01-14', 'Male', '+2348067890345', '9 Ikwerre Road, Port Harcourt', '2025-10-05 12:00:00', 'CARD6598234'),
        ('Aisha Yusuf', '2002-08-03', 'Female', '+2348139876542', '7 Maitama Crescent, Abuja', '2025-10-05 09:50:00','CARD00010'),
        ('Collins Ade', '1997-03-30', 'Male', '+2348125679087', '13 Challenge Road, Ibadan', '2025-10-06 08:10:00', 'CARD1982745'),
        ('Olamide Bamidele', '1999-07-02', 'Male', '+2348167890123', '4 Dugbe Street, Ibadan', '2025-10-06 18:25:00','CARD111245'),
        ('Jennifer Iroha', '2000-10-09', 'Female', '+2348115678901', '2 Ogui Road, Enugu', '2025-10-07 07:15:00', 'CARD6712098'),
        ('Victor Udo', '1996-11-19', 'Male', '+2348156789032', '8 Marian Road, Calabar', '2025-10-07 16:05:00', 'CARD48764640'),
        ('Ruth Akpan', '2001-09-13', 'Female', '+2348189234567', '6 Effiong Street, Uyo', '2025-10-08 14:20:00', 'CARD9856340'),
        ('Henry Adewale', '1998-05-25', 'Male', '+2348023456798', '10 Iwo Road, Ibadan', '2025-10-08 11:00:00', 'CARD0024879'),
        ('Esther Okon', '1999-03-07', 'Female', '+2348145678923', '14 Eket Close, Uyo', '2025-10-09 10:10:00', 'CARD2379401'),
        ('Matthew Obi', '1997-08-14', 'Male', '+2348076543219', '19 Upper Mission, Benin City', '2025-10-09 19:35:00', 'CARD4586342'),
        ('Peace Ajayi', '2002-07-22', 'Female', '+2349056789124', '4 Adeola Odeku Street, Lagos', '2025-10-10 08:40:00', 'CARD7802349'),
        ('Ifeanyi Okeke', '1995-10-02', 'Male', '+2348123456709', '21 New Market Road, Onitsha', '2025-10-10 17:00:00', 'CARD4875'),
        ('Grace Alabi', '1998-02-16', 'Female', '+2348087654390', '9 Marina Street, Lagos Island', '2025-10-11 09:30:00', 'CARD5647821'),
        ('Ahmed Sani', '2001-01-09', 'Male', '+2348109876523', '3 Sokoto Road, Kano', '2025-10-11 21:10:00', 'CARD48468'),
        ('Cynthia Eze', '1999-05-20', 'Female', '+2348145671234', '5 New Heaven Road, Enugu', '2025-10-12 10:15:00', 'CARD7821904'),
        ('Joseph Adamu', '1997-12-11', 'Male', '+2348095432123', '18 Ring Road, Jos', '2025-10-12 18:30:00', 'CARD47856311'),
        ('Martha Danjuma', '1996-04-18', 'Female', '+2348167894560', '20 Bauchi Road, Kaduna', '2025-10-13 07:00:00', 'CARD8910457'),
        ('Daniel Ibeh', '1995-06-10', 'Male', '+2348023450912', '16 Bode Thomas Street, Surulere, Lagos', '2025-10-13 16:50:00', 'CARD4845631'),
        ('Sophia Okpara', '2000-11-03', 'Female', '+2349034567810', '2 Ogui Layout, Enugu', '2025-10-14 12:40:00', 'CARD5637289'),
        ('Joshua Ojo', '1998-03-09', 'Male', '+2348115670983', '6 Oluyole Estate, Ibadan', '2025-10-14 20:25:00', 'CARD1203548'),
        ('Chidinma Nwachukwu', '1999-09-30', 'Female', '+2349051234567', '7 Ogba Road, Ikeja, Lagos', '2025-10-15 08:35:00', 'CARD8901763'),
        ('Emmanuel Ofor', '1996-07-17', 'Male', '+2348069871234', '4 New GRA, Enugu', '2025-10-15 19:10:00', 'CARD1200035'),
        ('Blessing Hassan', '1997-01-26', 'Female', '+2348102349087', '15 Ahmadu Bello Way, Abuja', '2025-10-16 09:00:00', 'CARD7293845'),
        ('Paul Edet', '1995-10-19', 'Male', '+2348023987456', '19 Marian Extension, Calabar', '2025-10-16 13:10:00', 'CARD1234026'),
        ('Nancy Umeh', '2001-08-23', 'Female', '+2348130987654', '6 Okpara Avenue, Enugu', '2025-10-17 11:55:00', 'CARD6384950'),
        ('Ishaq Abdullahi', '1998-01-12', 'Male', '+2348056789014', '10 Katsina Road, Kano', '2025-10-17 19:30:00', 'CARD7412569'),
        ('Precious Uka', '1999-12-24', 'Female', '+2348078912345', '8 Asaba Street, Owerri', '2025-10-18 07:15:00', 'CARD2083764'),
        ('Ebuka Nwafor', '1996-05-04', 'Male', '+2348169873456', '3 GRA Phase 2, Port Harcourt', '2025-10-18 17:20:00', 'CARD7854632'),
        ('Maryam Ibrahim', '1997-09-11', 'Female', '+2348145674321', '22 Sokoto Crescent, Kaduna', '2025-10-19 10:40:00', 'CARD9456238'),
        ('Kelvin Udoh', '1995-11-07', 'Male', '+2348034567123', '14 Udo Udoma Avenue, Uyo', '2025-10-19 18:05:00', 'CARD7563294'),
        ('Ogechi Nduka', '1998-07-25', 'Female', '+2348102345672', '11 Oguta Road, Onitsha', '2025-10-20 09:55:00', 'CARD1928347'),
        ('Tajudeen Lawal', '1996-02-02', 'Male', '+2348098765439', '5 Challenge Road, Ibadan', '2025-10-20 19:40:00', 'CARD7896542'),
        ('Chisom Opara', '1999-01-17', 'Female', '+2348156789043', '12 Uratta Road, Aba', '2025-10-21 08:50:00', 'CARD9083746'),
        ('Hassan Bello', '2000-05-29', 'Male', '+2348112345674', '17 Gwagwalada Street, Abuja', '2025-10-21 14:35:00', 'CARD1234567'),
        ('Joy Eze', '2002-06-13', 'Female', '+2348167890432', '9 Bishop Street, Nsukka', '2025-10-22 07:30:00', 'CARD5732901'),
        ('Ifeoluwa Adebisi', '1998-03-03', 'Male', '+2348023456123', '6 Bodija Area, Ibadan', '2025-10-22 18:00:00', 'CARD7542369'),
        ('Miriam Okeke', '1997-08-20', 'Female', '+2349035678902', '8 Old Road, Awka', '2025-10-23 09:20:00', 'CARD2390784'),
        ('Bashir Abdulkareem', '1996-10-08', 'Male', '+2348072340981', '12 Maiduguri Road, Kano', '2025-10-23 13:10:00', 'CARD5488643'),
        ('Amarachi Nwankwo', '1999-11-16', 'Female', '+2348150987654', '21 Aba-Owerri Road, Aba', '2025-10-24 10:05:00', 'CARD8573029'),
        ('Stephen Musa', '1995-09-06', 'Male', '+2348096543218', '10 Tudun Wada, Jos', '2025-10-24 19:20:00', 'CARD4867895'),
        ('Patience Udo', '2001-04-27', 'Female', '+2348039876543', '3 Ikot Ekpene Road, Uyo', '2025-10-25 08:45:00', 'CARD3752104'),
        ('Emmanuel James', '1997-12-22', 'Male', '+2348126549870', '4 Bank Road, Owerri', '2025-10-25 14:00:00', 'CARD7853332'),
        ('Victoria Adeyemi', '1998-09-09', 'Female', '+2348154321789', '2 Allen Avenue, Ikeja', '2025-10-26 10:50:00', 'CARD9012784'),
        ('Francis Nnamdi', '1996-03-15', 'Male', '+2348067892301', '13 Okigwe Road, Aba', '2025-10-26 16:45:00', 'CARD457596'),
        ('Halima Sulaiman', '1999-10-25', 'Female', '+2348091234561', '8 Bompai Road, Kano', '2025-10-27 09:30:00', 'CARD7319246')

    ]

    mycursor.executemany(addQuery,(value))
    mydb.commit()
    print("users added")

def add_patient():
    print("==========welcome to patient managment===============")
    print("Add a patient")

    fullname = input("please input patient fullname: ").strip().lower()
    dataofbirth = input("please input Date of Birth - DD/MM/YY: ").strip()
    gender = input("Enter Gender (MALE/FEMALE): ")
    contact = input("please enter phone number: ").strip()
    address = input("Enter house addresss: ")
    Reg_date = input("Enter date registered: ")
    Card_number = input("enter card number - CARDXXXXXXX: ")

    addQuery = "INSERT INTO patients (fullname,dateof_birth,gender,contact,address,date_registered,cardnumber) VALUE(%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(addQuery,(fullname,dataofbirth,gender,contact,address,Reg_date,Card_number))
    mydb.commit()
    print("user created")

def view_patients():
    print("list of patients")
    viewpatientsQuery = "SELECT * FROM patients"
    mycursor.execute(viewpatientsQuery)
    patient = mycursor.fetchall()
    header = ['fullname', 'dateof_birth', 'gender', 'contact', 'address', 'date_registered', 'cardnumber']
    print(tabulate(patient,headers=header,tablefmt="fancy_grid"))


def delete_patient():
    print("---------Delete Patients--------")
    view_patients()
    cardno = input("Enter Patient Card number: ").strip().lower()
    delete_query = "Delete from patients WHERE cardnumber = %s"
    mycursor.execute(delete_query,(cardno))
    mydb.commit()
    print("delete sucessful ✅")



def update_patients():
    view_patients()
    cardno = input("Enter Patient Card number: ").strip().lower()
    while True:
        print("what would you like to change")
        print("OPTION: ")
        print("1. Fullname ")
        print("2. Date of Birth")
        print("3. gender")
        print("4. contact")
        print("5. address")
        print("6. date_regitsered")
        print("7. card number")
        print("8. Exit")

        option = input("select an option: ")
        if option == "1":
            new_data = input("input new Fullname: ")
            updateQuery = "UPDATE patients SET fullname = %s WHERE cardnumber = %s"
            mycursor.execute(updateQuery,(new_data,cardno))
            mydb.commit()
            print("successfully updated")

        elif option == '2':
            new_data = input("input new Date of Birth: ")
            updateQuery = "UPDATE patients SET Dateof_Birth = %s WHERE cardnumber = %s"
            mycursor.execute(updateQuery,(new_data,cardno))
            mydb.commit()
            print("successfully updated")

        elif option == '3':
            new_data = input("input new gender: ")
            updateQuery = "UPDATE patients SET gender = %s WHERE cardnumber = %s"
            mycursor.execute(updateQuery,(new_data,cardno))
            mydb.commit()
            print("successfully updated")
        
        elif option == '4':
            new_data = input("input new contact: ")
            updateQuery = "UPDATE patients SET contact = %s WHERE cardnumber = %s"
            mycursor.execute(updateQuery,(new_data,cardno))
            mydb.commit()
            print("successfully updated")

        elif option == '5':
            new_data = input("input new address: ")
            updateQuery = "UPDATE patients SET address = %s WHERE cardnumber = %s"
            mycursor.execute(updateQuery,(new_data,cardno))
            mydb.commit()
            print("successfully updated")

        elif option == '6':
            new_data = input("input new date_registered: ")
            updateQuery = "UPDATE patients SET date_registered = %s WHERE cardnumber = %s"
            mycursor.execute(updateQuery,(new_data,cardno))
            mydb.commit()
            print("successfully updated")

        elif option == '7':
            new_data = input("input new Card number: ")
            updateQuery = "UPDATE patients SET cardnumber = %s WHERE cardnumber = %s"
            mycursor.execute(updateQuery,(new_data,cardno))
            mydb.commit()
            print("successfully updated")
        
        elif option == "8":
            break

        else:
            print("invalid")
update_patients()