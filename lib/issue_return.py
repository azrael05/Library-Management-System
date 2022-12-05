def issue_book(id,database):
    cursor=database.cursor()
    sql="UPDATE books SET available = available - 1  WHERE id={id}".format(id=str(id))
    cursor.execute(sql)
    sql="INSERT INTO records VALUES"
    database.commit()

def return_book(id,database):
    cursor=database.cursor()
    sql="UPDATE books SET available = available + 1  WHERE id={id}".format(id=str(id))
    cursor.execute(sql)
    database.commit()