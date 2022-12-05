import sys
sys.path.insert(0,"./User_Management")
from User import USER
from Pretty_table_converter import convert_to_pretty_table
def create_new_user(database,users):
    cursor=database.cursor()
    for user in users:
        cursor.execute("INSERT INTO users(name,password,role) VALUES ('{name}','{password}','{role}')".format(name=user.name,password=user.password,role=user.role))
        cursor.execute("SELECT * FROM users WHERE name='{name}' AND password='{password}' AND role='{role}'".format(name=user.name,password=user.password,role=user.role))
        convert_to_pretty_table(cursor)
    database.commit()
        
def list_users(database):
    cursor=database.cursor()
    cursor.execute("SELECT * FROM users")
    convert_to_pretty_table(cursor)
    

def remove_user(database):
    cursor=database.cursor()
    username=input("Enter username")
    id=input("Enter id")
    cursor.execute("DELETE FROM users WHERE name='{username}' AND id={id}".format(username=username,id=id))
    database.commit()

def search_user(database):
    id=input("Enter id")
    cursor=database.cursor()
    cursor.execute("SELECT * FROM users WHERE id={id}".format(id=id))
    convert_to_pretty_table(cursor)
