import mysql.connector
import sys
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="library")

cursor=mydb.cursor()
cursor.execute("SELECT * FROM books LIMIT 5")

convert_to_pretty_table(cursor)
cursor.execute("DROP USER devesh@localhost")
cursor.execute("CREATE USER IF NOT EXISTS devesh@localhost IDENTIFIED BY 'password'")
cursor.execute("GRANT SELECT ON library.* TO devesh@localhost")
cursor.execute("SELECT USER FROM mysql.user ")
for user in cursor:
    print(user)

cursor.execute("SELECT current_user()")
for user in cursor:
    print("Current user is-",user)
mydb.commit()
mydb.close()
mydb=mysql.connector.connect(
    host="localhost",
    user="devesh",
    password="password",
    database="library")
cursor=mydb.cursor()
cursor.execute("SELECT current_user()")
for user in cursor:
    print("Current user is-",user)
cursor.execute("SELECT * FROM books LIMIT 5")
convert_to_pretty_table(cursor)

# cursor.execute("UPDATE books SET title='your tits'  WHERE id=1")
cursor.execute("SELECT * from books WHERE id=1")
convert_to_pretty_table(cursor)