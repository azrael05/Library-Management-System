import sys
sys.path.insert(0,"./Books")
def get_book_details(database,id):
    from Pretty_table_converter import convert_to_pretty_table
    mycursor=database.cursor()
    if not id:
        id=input("Enter the id of the book: ")
    if not id:
        title=input("Enter the title of the book: ")
        author=input("Enter the author of the book: ")
    sql="SELECT * FROM books WHERE id={id}".format(id=str(id))
    if not id:
        sql="SELECT * FROM books WHERE title LIKE '%{title}%' AND author LIKE '%{author}%'".format(title=str(title), author=str(author))
    mycursor.execute(sql)
    convert_to_pretty_table(mycursor)



def list_all_book(database,role):
    from Pretty_table_converter import convert_to_pretty_table
    mycursor=database.cursor()
    if(role=="admin"):
        mycursor.execute("SELECT * FROM books")
    if(role=="student"):
        mycursor.execute("SELECT id,title,author FROM books")
    convert_to_pretty_table(mycursor)



def search_book(database):
    from Pretty_table_converter import convert_to_pretty_table
    mycursor=database.cursor()
    title=input("Enter the title of the book: ")
    author=input("Enter the author of the book: ")
    sql="SELECT id,title,author FROM books WHERE title LIKE '%{title}%' AND author LIKE '%{author}%'".format(title=str(title), author=str(author))
    mycursor.execute(sql)
    convert_to_pretty_table(mycursor)