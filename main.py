 
from login import login
from student import *
from admin import *
mydb=login()
print("Choose options 1. student 2.admin")
choice=int(input())
if choice==1:
    student(mydb)
else:
    admin(mydb)
