import sys
sys.path.insert(0,"../")
import datetime
def issue_book(database,userid,id):
    cursor=database.cursor()
    username=None
    cursor.execute("SELECT name from users WHERE id={userid}".format(userid=userid))
    for x in cursor:
        username=x[0]
    if(username==None):
        print("Invalid username")
        return -1
    cursor.execute("SELECT available FROM books WHERE id={id}".format(id=id))
    e=0
    for x in cursor:
        e=1
        if(x[0]==0):
            print("Unavailable")
            return -1
    if e==0:
        print("Invalid book")
        return -1
    sql="UPDATE books SET available = available - 1  WHERE id={id}".format(id=id)
    cursor.execute(sql)

    sql="INSERT INTO records(userid,username,id,issue_date) VALUES ({userid},'{username}',{id},CURDATE())".format(userid=userid,username=username,id=id)
    cursor.execute(sql)
    print("Book issued\n Date of return - ", datetime.date.today()+datetime.timedelta(days=21))
    database.commit()

def return_book(database,userid,id):
    cursor=database.cursor()
    sql="UPDATE books SET available = available + 1  WHERE id={id}".format(id=str(id))
    cursor.execute(sql)
    sql="UPDATE records SET return_date = CURDATE() WHERE userid='{userid}' AND id={id} AND return_date IS NULL".format(userid=userid,id=id)
    cursor.execute(sql)
    database.commit()

def get_list_issued(database):
    from Pretty_table_converter import convert_to_pretty_table
    cursor=database.cursor()
    sql="SELECT username,expected_return_date FROM records WHERE overtime IS NULL"
    cursor.execute(sql)
    convert_to_pretty_table(cursor)

def get_overdue_list(database):
    from Pretty_table_converter import convert_to_pretty_table
    cursor=database.cursor()
    sql="SELECT username, id,issue_date, DATEDIFF(CURDATE(),issue_date) as overdue_by FROM records WHERE DATEDIFF(CURDATE(),issue_date)>21 and return_date is NULL"
    cursor.execute(sql)
    convert_to_pretty_table(cursor)