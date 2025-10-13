import pymysql

mydb = pymysql.connect(
    host="localhost",
    port=3307,
    user="Admin",
    password="myAdmin",
    database="hospitalDB" 
)

mycursor = mydb.cursor()
print("connected succfully")