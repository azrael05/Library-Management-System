import mysql.connector
from book_info import Book  

def convert_to_pretty_table(cursor):
    from prettytable import PrettyTable
  
    # Specify the Column Names while initializing the Table
    column_names=[]

    for x in cursor.description:
        column_names.append(x[0])
    myTable = PrettyTable(column_names)
    
    for x in cursor:
        myTable.add_row(list(x))
    
    print(myTable)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="library"
)
def add_book(books,mycursor):
    for book in books:
        try:
            sql = "INSERT INTO books (title, author, quantity, available) VALUES " +str((book.title, book.author, book.quantity, book.quantity))
            mycursor.execute(sql)
        
        except:
            sql="UPDATE books SET quantity = quantity + {quantity}, available=available + {quantity} WHERE title = '{title}' AND author = '{author}'".format(quantity=str(book.quantity), title=str(book.title), author=str(book.author))
            mycursor.execute(sql)
    print("Books added successfully")
    mydb.commit()

def issue_book(id,mycursor):
    sql="UPDATE books SET available = available - 1  WHERE id={id}".format(id=str(id))
    mycursor.execute(sql)
    mydb.commit()

def return_book(id,mycursor):
    sql="UPDATE books SET available = available + 1  WHERE id={id}".format(id=str(id))
    mycursor.execute(sql)
    mydb.commit()

def search_book(mycursor):
    title=input("Enter the title of the book: ")
    author=input("Enter the author of the book: ")
    sql="SELECT id,title,author FROM books WHERE title LIKE '%{title}%' AND author LIKE '%{author}%'".format(title=str(title), author=str(author))
    mycursor.execute(sql)
    convert_to_pretty_table(mycursor)

def list_all_book(mycursor):
    mycursor.execute("SELECT * FROM books")
    convert_to_pretty_table(mycursor)

def get_book_details(mycursor):
    id=input("Enter the id of the book: ")
    if not id:
        title=input("Enter the title of the book: ")
        author=input("Enter the author of the book: ")
    sql="SELECT * FROM books WHERE id={id}".format(id=str(id))
    if not id:
        sql="SELECT * FROM books WHERE title LIKE '%{title}%' AND author LIKE '%{author}%'".format(title=str(title), author=str(author))
    mycursor.execute(sql)
    convert_to_pretty_table(mycursor)

def add_book_from_excel(mycursor,excel_file):
    import pandas as pd
    df=pd.read_csv(excel_file,header=0)
    books=[]
    if not "quantity" in df.columns:
        df['quantity']=1
    print(df.head(5))
    for index, row in df.iterrows():
        books.append(Book(row['title'],row['author'],row['quantity']))
    add_book(books,mycursor)
    print("Added {num} books.".format(num=str(len(books))))
    mycursor.execute("SELECT COUNT(DISTINCT title,author) FROM books")
    for x in mycursor:
        print("Total number of books in the library: {num}".format(num=str(x[0])))

def delete_all_books(mycursor):
    mycursor.execute("DELETE FROM books")
    mydb.commit()
    print("All books deleted successfully")

mycursor = mydb.cursor()
# mycursor.execute("DROP TABLE if exists books")
try:
    mycursor.execute("CREATE TABLE books (id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(255), author VARCHAR(255), quantity INT, available INT, UNIQUE (title, author))")
except:
    pass

ch=1
while(ch!=7):
    print("Available Choices \n1. Add a book \n2. Issue a book \n3. Return a book \n4. Search a book \n5. List all books \n6. Get book details \n7. Delete all books \n8.Exit")
    ch=int(input())
    if ch==1:
        print("Press 1 for manual adding and 2 for excel file")
        ch1=int(input())
        if ch1==1:
            print("Enter number of books")
            num_of_books=int(input())
            books=[]
            for i in range(num_of_books):
                title=input("Enter the title of the book: ")
                author=input("Enter the author of the book: ")
                quantity=input("Enter the quantity of the book: ")
                books.append(Book(title,author,quantity))
        add_book(books,mycursor)
        if ch1==2:
            print("Enter the path of the excel file")
            path=input()
            add_book_from_excel(mycursor,path)
    elif ch==2:
        id=int(input("Enter the id of the book: "))
        issue_book(id,mycursor)
    elif ch==3:
        id=int(input("Enter the id of the book: "))
        return_book(id,mycursor)
    elif ch==4:
        search_book(mycursor)
    elif ch==5:
        list_all_book(mycursor)
    elif ch==6:
        get_book_details(mycursor)
    elif ch==7:
        delete_all_books(mycursor)