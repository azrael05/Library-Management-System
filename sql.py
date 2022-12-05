import mysql.connector
from User_Management.User import USER
from User_Management.user_management import create_new_user
def Add_user_from_excel(file_path):
    import pandas as pd
    df=pd.read_excel(file_path)
    print(df)
    for index,rows in df.iterrows():
        user=USER(rows["Name"],rows["Password"],rows["Role"])
        create_new_user(mydb,user)


mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="password",
)

cursor=mydb.cursor()
# cursor.execute("CREATE DATABASE IF NOT EXISTS library")
mydb.connect(database="library")
# cursor.execute("DROP TABLE IF EXISTS books")
# cursor.execute("CREATE TABLE books (id INT AUTO_INCREMENT PRIMARY , title VARCHAR(255), author VARCHAR(255), quantity INT ,available INT)")
# cursor.execute("DROP TABLE IF EXISTS records")
# cursor.execute("CREATE TABLE records (username VARCHAR(255) NOT NULL,id INT , issue_date DATE, expected_return_date DATE GENERATED ALWAYS AS (ADDDATE(issue_date,21)), return_date DATE DEFAULT NULL, overtime VARCHAR(5) GENERATED ALWAYS AS (CASE WHEN return_date IS NULL THEN NULL WHEN return_date-issue_date>21 THEN \"YES\" ELSE \"NO\" END))")
# cursor.execute("DROP TABLE IF EXISTS users")
# cursor.execute("CREATE TABLE users (username VARCHAR(255) PRIMARY KEY, role VARCHAR(255)")
from Books.Modify_Info import add_book_from_excel
# add_book_from_excel(mydb,r"Demo files\bohemian_literature.csv")
Add_user_from_excel(r"Demo files\user.xlsx")
