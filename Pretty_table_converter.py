def convert_to_pretty_table(cursor):
    from prettytable import PrettyTable
  
    # Specify the Column Names while initializing the Table
    column_names=[]

    for x in cursor.description:
        column_names.append(x[0])
    myTable = PrettyTable(column_names)
    
    for x in cursor:
        myTable.add_row(list(x))
    
    print(myTable)