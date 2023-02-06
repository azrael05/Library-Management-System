 
from student import *
from admin import *
def login():
    import mysql.connector
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="library"
    )
    cursor=mydb.cursor()
    cursor.execute("SELECT * FROM users")
    convert_to_pretty_table(cursor)
    id=input("Enter id: ")
    password=input("Enter password: ")
    cursor.execute("SELECT role FROM users WHERE id={id} AND password='{password}'".format(id=id,password=password))
    role=None
    for x in cursor:
        role=x[0]
    mydb.disconnect()
    mydb.close()
    print("hello")
    del mydb
    if(role=="student"):
        mydb=mysql.connector.connect(
        host="localhost",
        user="students",
        password="password",
        database="library"
        )
        student(mydb)
    elif(role=="admin"):
        mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="library"
        )
        admin(mydb)
    else:
        print("Invalid Credentials")
        exit()


mydb=login()
    
