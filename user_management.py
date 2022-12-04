import mysql.connector
from User_details import USER
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
    database="library"
)
print("Enter user name for new user")
username=input()
print("Enter password for new user")
password=input()
print("Enter role for new user")
role=input()
cursor=mydb.cursor()
user=USER(username,password,role)
cursor.execute("CREATE USER IF NOT EXISTS {username}@localhost IDENTIFIED BY '{password}'".format(username=user.name,password=user.password))
if(user.role=="Admin"):
    cursor.execute("GRANT ALL PRIVILEGES TO {username}@localhost ON library.*")
else:
    cursor.execute("GRANT SELECT TO {username}@localhost ON library.*")
