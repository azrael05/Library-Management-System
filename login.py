class credentials():
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password

def login():
    import mysql.connector
    username=input("Enter username: ")
    password=input("Enter password: ")
    user=credentials(username,password)
    
    mydb=mysql.connector.connect(
    host="localhost",
    user=user.username,
    password=user.password,
    database="library"
    )
    return mydb
    