# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     username="root",
#     password="password",
# )

# cursor=mydb.cursor()
# cursor.execute("CREATE DATABASE IF NOT EXISTS library")
# mydb.connect(database="library")
# cursor.execute("DROP TABLE IF EXISTS books")
# cursor.execute("CREATE TABLE books (id INT AUTO_INCREMENT PRIMARY , )"
# cursor.execute("DROP TABLE IF EXISTS records")
# cursor.execute("CREATE TABLE records (username VARCHAR(255) NOT NULL,id INT , issue_date DATE, expected_return_date DATE GENERATED ALWAYS AS (ADDDATE(issue_date,21)), return_date DATE DEFAULT NULL, overtime VARCHAR(5) GENERATED ALWAYS AS (CASE WHEN return_date IS NULL THEN NULL WHEN return_date-issue_date>21 THEN \"YES\" ELSE \"NO\" END))")
values={1:"Add a book",
        2:"Issue a book",
        3:"Return a book",
        4:"Search a book",
        5:"List all books",
        6:"Get book details",
        7:"Delete all books",
        8:"Remove a book",
        9:"Create new user",
        10:"List all users",
        11:"Search User",
        12:"Exit",
        }

for i in sorted(values.keys()):
    print("{i} - {val}".format(i=i,val=values[i]))

print("alca"=="ala")