from Books.Read_Info import *
from Books.Modify_Info import *
from Books.book import Book
from lib.issue_return import *
from pathlib import WindowsPath
from User_Management.user_management import *
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
        12:"See list of current issued",
        13:"Exit",
        }
def admin(database):
    ch=1
    while(ch!=12):
        for i in sorted(values.keys()):
            print("{i} - {val}".format(i=i,val=values[i]))
        ch=int(input())
        if values[ch]=="Add a book":
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
                add_book(database,books)
            if ch1==2:
                print("Enter the path of the excel file")
                path=WindowsPath(input())
                add_book_from_excel(database,path)
        elif values[ch]=="Issue a book":
            username=input("Enter username")
            id=int(input("Enter the id of the book: "))
            issue_book(database,username,id)
        elif values[ch]=="Return a book":
            username=input("Enter username")
            id=int(input("Enter the id of the book: "))
            return_book(database,username,id)
        elif values[ch]=="Search a book":
            search_book(database)
        elif values[ch]=="List all books":
            list_all_book(database,"admin")

        elif values[ch]=="Get book details":
            id=int(input("Enter book id"))
            get_book_details(database,id)

        elif values[ch]=="Remove a book":
            remove_book(database)

        elif values[ch]=="Create new user":
            print("Enter user name for new user")
            username=input()
            print("Enter password for new user")
            password=input()
            print("Enter role for new user")
            role=input()
            from User_Management.User import USER
            user=USER(username,password,role)
            create_new_user(database,user)
        elif values[ch]=="List all users":
            list_users(database)
        elif values[ch]=="Search User":
            search_user(database)
        elif values[ch]=="See list of current issued":
            get_list_issued(database)
        elif values[ch]=="Exit": 
            break
        print("press key to continue")
        input()