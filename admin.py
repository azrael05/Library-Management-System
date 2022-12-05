from Books.Read_Info import *
from Books.Modify_Info import *
from Books.book import Book

def admin(mydatabase):
    cursor=mydatabase.cursor()
    ch=1
    while(ch!=8):
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
                add_book(books,mydatabase)
            if ch1==2:
                print("Enter the path of the excel file")
                path=input()
                add_book_from_excel(mydatabase,path)
        # elif ch==2:
        #     id=int(input("Enter the id of the book: "))
        #     issue_book(id,mycursor)
        # elif ch==3:
        #     id=int(input("Enter the id of the book: "))
        #     return_book(id,mycursor)
        if ch==4:
            search_book(mydatabase,id)
        elif ch==5:
            list_all_book(mydatabase)
        elif ch==6:
            get_book_details(mydatabase)
        elif ch==7:
            delete_all_books(mydatabase)
        # elif ch==:
        #     add_new_user()
        # elif ch==:
        #     get_list_of_issued()
        # elif ch==8:
        #     logout(database)
        elif ch==8: 
            break
        print("press key to continue")
        input()