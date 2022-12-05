import sys
sys.path.insert(0,"../")
def issue_book(database,username,id):
    cursor=database.cursor()
    cursor.execute("SELECT available FROM books WHERE id={id}".format(id=id))
    for x in cursor:
        if(x[0]==0):
            print("Unavailable")
            return -1
    sql="UPDATE books SET available = available - 1  WHERE id={id}".format(id=id)
    cursor.execute(sql)

    sql="INSERT INTO records(username,id,issue_date) VALUES ('{username}',{id},CURDATE())".format(username=username,id=id)
    cursor.execute(sql)
    
    database.commit()

def return_book(database,username,id):
    cursor=database.cursor()
    sql="UPDATE books SET available = available + 1  WHERE id={id}".format(id=str(id))
    cursor.execute(sql)
    sql="UPDATE records SET return_date = CURDATE() WHERE username='{username}' AND id={id} AND return_date IS NULL".format(username=username,id=id)
    cursor.execute(sql)
    database.commit()

def get_list_issued(database):
    from Pretty_table_converter import convert_to_pretty_table
    cursor=database.cursor()
    sql="SELECT username,expected_return_date FROM records WHERE overtime IS NULL"
    cursor.execute(sql)
    convert_to_pretty_table(cursor)