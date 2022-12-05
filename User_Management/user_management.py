import sys
sys.path.insert(0,"./User_Management")
from User import USER
def create_new_user(database):
    print("Enter user name for new user")
    username=input()
    print("Enter password for new user")
    password=input()
    print("Enter role for new user")
    role=input()
    cursor=database.cursor()
    user=USER(username,password,role)
    while(True):
        try:
            cursor.execute("CREATE USER {username}@localhost IDENTIFIED BY '{password}'".format(username=user.name,password=user.password))
            break
        except:
            print("Username already exists")
    if(user.role.lower()=="admin"):
        cursor.execute("GRANT ALL PRIVILEGES TO {username}@localhost ON library.*")
    elif(user.role.lower()=="student"):
        cursor.execute("GRANT SELECT TO {username}@localhost ON library.books")
    database.commit()

def list_users(database):
    cursor=database.cursor()
    cursor.execute("SELECT user FROM mysql.user")
    for x in cursor:
        print(x)

def remove_user(database):
    cursor=database.cursor()
    username=input("Enter username")
    cursor.execute("DELETE FROM mysql.user WHERE user='{username}'".format(username=username))
    database.commit()

def search_user(database):
    username=input("Enter username")
    cursor=database.cursor()
    cursor.execute("SELECT user FROM mysql.user WHERE user LIKE %{username}%".format(username=username))
    for x in cursor:
        print(x)
