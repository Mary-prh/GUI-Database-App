import sqlite3


def connect():
    # 1. Connect to a database
    conn = sqlite3.connect("Books.db")
    # 2. Create a cursor object
    curs = conn.cursor()
    # 3. write an sql query
    curs.execute("CREATE TABLE IF NOT EXISTS BookStore (ID INTEGER PRIMARY KEY , title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    # 4. Commit the changes
    conn.commit()
    # 5. Close the database
    conn.close()

# View All from the table
def view():
    # 1. Connect to a database
    conn = sqlite3.connect("Books.db")
    # 2. Create a cursor object
    curs = conn.cursor()
    curs.execute("SELECT * FROM BookStore") # selects all from BookStore table
    rows = curs.fetchall()
    conn.close()
    return rows


# Search Function
def search(title="",author="",year="",isbn=""): #empty value lets the user to search with only one keyword as well
    # 1. Connect to a database
    conn = sqlite3.connect("Books.db")
    # 2. Create a cursor object
    curs = conn.cursor()
    # 3. write an sql query
    curs.execute("SELECT * FROM BookStore WHERE title =? OR author=? OR year=? OR isbn=?", (title,author,year,isbn) )
    rows = curs.fetchall()
    conn.close()
    return rows


# Add Entry into the database
def insert(title,author,year,isbn):
    # 1. Connect to a database
    conn = sqlite3.connect("Books.db")
    # 2. Create a cursor object
    curs = conn.cursor()
    # 3. write an sql query
    curs.execute("INSERT INTO BookStore VALUES(null,?,?,?,?)",(title,author,year,isbn))
    # 4. Commit the changes
    conn.commit()
    # 5. Close the database
    conn.close()


# Update Entry
def Update(ID,title,author,year,isbn):
    # 1. Connect to a database
    conn = sqlite3.connect("Books.db")
    # 2. Create a cursor object
    curs = conn.cursor()
    curs.execute("UPDATE BookStore SET title =?, author=?, year=?, isbn=? WHERE ID =?",(title,author,year,isbn,ID)) # note the order of variables
    conn.commit() #because we need to update the changes
    conn.close() 


# Delete some rows from the data
def delete(ID):
    # 1. Connect to a database
    conn = sqlite3.connect("Books.db")
    # 2. Create a cursor object
    curs = conn.cursor()
    curs.execute("DELETE FROM BookStore WHERE ID=?",(ID,))
    conn.commit() #because we need to update the changes
    conn.close()


# Close the window

connect() # this is necessary so the function be executed when it is called by the frontend
#insert("The Atlas of the Land", "Karen Wynn", 1985, 9780345314314)
# delete(6)
Update(2, "Plausible Prejudices", "Joseph Epstein", 1985, 9780393019186)
print(view())
# print(search("The Atlas of the Land"))
# or
# print(search(author = "The Atlas of the Land"))
