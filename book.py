class Book():
    
    def __init__(self, title, author, quantity=1):
        self.title = title
        self.author = author
        self.quantity = quantity

def get_book_details(mycursor,id):
    from Pretty_table_converter import convert_to_pretty_table
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

def list_all_book(mycursor):
    from Pretty_table_converter import convert_to_pretty_table
    mycursor.execute("SELECT * FROM books")
    convert_to_pretty_table(mycursor)

def search_book(mycursor):
    from Pretty_table_converter import convert_to_pretty_table
    title=input("Enter the title of the book: ")
    author=input("Enter the author of the book: ")
    sql="SELECT id,title,author FROM books WHERE title LIKE '%{title}%' AND author LIKE '%{author}%'".format(title=str(title), author=str(author))
    mycursor.execute(sql)
    convert_to_pretty_table(mycursor)