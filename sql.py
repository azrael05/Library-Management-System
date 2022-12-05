import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="password",
    database="library"
)
cursor=mydb.cursor()
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)
cursor.execute("DROP TABLE IF EXISTS records ")
cursor.execute("CREATE TABLE records (username VARCHAR(255) NOT NULL,id INT , issue_date DATE, expected_return_date DATE GENERATED ALWAYS AS (ADDDATE(issue_date,21)), return_date DATE DEFAULT NULL, overtime VARCHAR(5) GENERATED ALWAYS AS (CASE WHEN return_date IS NULL THEN NULL WHEN return_date-issue_date>21 THEN \"YES\" ELSE \"NO\" END))")
# cursor.execute("INSERT INTO records(username, issue_date) VALUES (\"devesh\",\"2022-10-25\")")
# cursor.execute("SELECT * FROM records")
# cursor.execute("SELECT DATE_ADD('2020-11-12', INTERVAL 10 DAY)")
# for x in cursor:
#     print(x)