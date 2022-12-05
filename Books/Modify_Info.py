#Adding Functions

def add_book(database,books):
    mycursor=database.cursor()
    for book in books:
        try:
            sql = "INSERT INTO books (title, author, quantity, available) VALUES " +str((book.title, book.author, book.quantity, book.quantity))
            mycursor.execute(sql)
        
        except:
            sql="UPDATE books SET quantity = quantity + {quantity}, available=available + {quantity} WHERE title = '{title}' AND author = '{author}'".format(quantity=str(book.quantity), title=str(book.title), author=str(book.author))
            mycursor.execute(sql)
    print("Books added successfully")
    database.commit()

def add_book_from_excel(database,excel_file):
    import pandas as pd
    from book import Book

    cursor=database.cursor()
    df=pd.read_csv(excel_file,header=0)
    books=[]
    if not "quantity" in df.columns:
        df['quantity']=1
    print(df.head(5))
    for index, row in df.iterrows():
        books.append(Book(row['title'],row['author'],row['quantity']))
    add_book(database,books)
    print("Added {num} books.".format(num=str(len(books))))
    cursor.execute("SELECT COUNT(DISTINCT title,author) FROM books")
    for x in cursor:
        print("Total number of books in the library: {num}".format(num=str(x[0])))




## Removing Functions
import sys
sys.path.insert(0,"./Books")
from Read_Info import *
def delete_all_books(database):
    cursor=database.cursor()
    cursor.execute("DELETE FROM books")
    database.commit()
    print("All books deleted successfully")

def remove_book(database):
    print("Enter book id")
    id=int(input())
    get_book_details(database,id)
    cursor=database.cursor()
    cursor.execute("DELETE FROM books where id='{id}'".format(id=id))
    database.commit()