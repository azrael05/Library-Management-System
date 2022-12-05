def issue_book(username,id,database):
    cursor=database.cursor()

    sql="UPDATE books SET available = available - 1  WHERE id={id}".format(id=str(id))
    cursor.execute(sql)

    sql="INSERT INTO records(username,id,issue_date) VALUES ('{username}',{id},CURDATE())".format(username=username,id=id)
    cursor.execute(sql)
    
    database.commit()

def return_book(username,id,database):
    cursor=database.cursor()
    sql="UPDATE books SET available = available + 1  WHERE id={id}".format(id=str(id))
    cursor.execute(sql)
    sql="UPDATE records SET return_date = CURDATE() where username='{username}' AND id={id} AND return_date=NULL".format(username=username,id=id)
    cursor.execute(sql)
    database.commit()
