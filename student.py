from Books.Read_Info import *
values={1:"Search a book",
        2:"List all books",
        3:"Get book details",
        5:"Exit",
        }
def student(mydatabase):
    ch=1
    while(ch!=5):
        for i in sorted(values.keys()):
            print("{i} - {val}".format(i=i,val=values[i]))
        ch=int(input())
        if values[ch]=="Search a book":
            search_book(mydatabase)
        elif values[ch]=="List all books":
            list_all_book(mydatabase,"student")
        elif values[ch]=="Get book details":
            id=input("Enter book id")
            get_book_details(mydatabase,id)
        # elif values[ch]==4:
        #     logout(mydatabase)
        elif values[ch]=="Exit": 
            break
        else:
            print("Enter Valid Input")
            continue
        print("press key to continue")
        input()