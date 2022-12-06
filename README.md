# Library-Management-System

## Required Libraries and software
1. Mysql (8.0 or greater)
2. Pretty Table
3. Pandas
4. Python3


## Steps to run
1. Clone this repository.
2. Run sql.py for creating database, populate the tables with sample data.
3. Run main.py to test the management system.
<br>Note - Check password and name for of account during initial run of sql.py.

<br><br><br>
## About the system
There are two types of users and their rights are 
1. Admin - modify records for issue and return, search and modify book records, search and modify users (admin and student), see list of overdue books, see list of currently due books
2. Student - Search for books and see availability of the book

<br><br><br><br>
## There are three tables in the database:-
1. Books: to store all the details of book with the following schema 
- Book id INT: auto-generated
- Book Title STRING
- Author STRING
- Quantity INT: to denote the total quantity of the book in the library
- Available INT: to show no. of those book currently available in library

2. Records: To store issue and return details
- User id INT: to denote user
- Book id INT: to denote book
- User name STRING: to see the name of the person
- Issue date DATE
- Expected Return Date DATE:  Auto generated from issue date as issue date + 21
- Return Date DATE:  NULL till the book has been returned
- Overtime BOOL: AUTO GENERATED Whether the return date exceeded the due time

3. Users: To store user details
- User id INT: Auto generated
- User name STRING: user name
- Password STRING: Required for logging in to avail services 
- Role STRING: Admin or student to give me required rights on sign in
