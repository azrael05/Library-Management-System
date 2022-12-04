from book import get_book_details
def delete_all_books(database):
    cursor=database.cursor()
    cursor.execute("DELETE FROM books")
    database.commit()
    print("All books deleted successfully")

def remove_book(database):
    print("Enter book id")
    id=int(input())
    get_book_details(cursor,id)
    cursor=database.cursor()
    cursor.execute("DELETE * FROM book where id={id}".format(id=id))