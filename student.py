from Books.Read_Info import *
def student(mydatabase):
    ch=1
    while(ch!=5):
        print("Available Choices \n1. Search a book \n2. List all books \n3. Get book details \n4. Logout \n5. Exit")
        ch=int(input())
        if ch==1:
            search_book(mydatabase)
        elif ch==2:
            list_all_book(mydatabase,"student")
        elif ch==3:
            id=input("Enter book id")
            get_book_details(mydatabase,id)
        # elif ch==4:
        #     logout(mydatabase)
        elif ch==5: 
            break
        else:
            print("Enter Valid Input")
            continue
        print("press key to continue")
        input()