def add_book(books,database):
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
    add_book(books,cursor)
    print("Added {num} books.".format(num=str(len(books))))
    cursor.execute("SELECT COUNT(DISTINCT title,author) FROM books")
    for x in cursor:
        print("Total number of books in the library: {num}".format(num=str(x[0])))