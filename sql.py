import mysql.connector
# class book:
#     def __init__(self,title,author,quantity=1):
#         self.title = title
#         self.author = author
#         self.quantity = quantity
# def add_book(book,mydb):
#     mycursor = mydb.cursor()
#     mycursor.execute("INSERT INTO books (title,author,quantity) VALUES (%s,%s,%s)",(book.title,book.author,book.quantity))
#     # mycursor.execute("IF EXISTS (SELECT title,author FROM books WHERE title = %s AND author = %s)", (book.title,book.author))
#                     # BEGIN UPDATE books SET quantity = quantity + 1 AND available = available + 1 WHERE title = %s AND author = %s END ELSE BEGIN INSERT INTO books (title,author,quantity,available) VALUES (%s,%s,%s,%s)",(book.title,book.author,book.title,book.author,book.title,book.author,book.quantity,book.quantity))
#     mydb.commit()   
def convert_to_pretty_table(cursor):
    from prettytable import PrettyTable
  
# Specify the Column Names while initializing the Table
    myTable = PrettyTable(["Student Name", "Class", "Section", "Percentage"])
    
    for x in cursor:
        myTable.add_row(list(x))
    
    print(myTable)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="library"
)

mycursor = mydb.cursor()
# # mycursor.execute("DROP TABLE if exists books")
# try:
#     mycursor.execute("CREATE TABLE books (id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(255), author VARCHAR(255), quantity INT, available INT)")
#     print("hello")
# except:
#     pass
# # mycursor.execute("ALTER TABLE books ADD PRIMARY KEY(title)")
# print("Database and table created successfully")
# # book={'title':'The Alchemist','author':'Paul'}
# # mycursor.execute("SELECT * FROM books")
# # for x in mycursor:
# #     print(x)
# new_book=book('newsdafas','sadasd')
# # add_book(new_book,mydb)
# mycursor.execute("SELECT * FROM books")
# print("All books present in database are")
# for x in mycursor:
#     print(x)
# mycursor.execute("IF (SELECT EXISTS(SELECT * FROM books WHERE title = 'The Alchemist' AND author = 'Paul')) IS NOT NULL BEGIN UPDATE books SET quantity = quantity + 1 AND available = available + 1 WHERE title = 'The Alchemist' AND author = 'Paul")
# print("The book you are looking for is")
# for x in mycursor:
#     print(x)
# mycursor.execute("CREATE TABLE testing(id INT,name VARCHAR(255))")
# print("Table created successfully")
# mycursor.execute("INSERT INTO testing (id,name) VALUES (%s,%s)",(1,'hello'))
# mycursor.execute("INSERT INTO testing (id,name) VALUES (%s,%s)",(2,'hello'))
# mycursor.execute("IF (SELECT 1 FROM (SELECT EXISTS(SELECT * FROM testing WHERE id = 1)))=0 BEGIN INSERT INTO testing (id,name) VALUES (%s,%s) END",(6,'hello'))
# mycursor.execute("DESCRIBE testing")
mycursor.execute("SELECT * FROM testing")
for x in mycursor:
    print(x)

print(mycursor.description[:,0])
# mydb.commit() 