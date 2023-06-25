you can use ur own database as well as table.......

import mysql.connector

def create_database():
    # establish connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="urpassword"
    )

    # new database creation
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE lib")
    print("DATABASE CREATED SUCCESSFULLY!")

    # CONNECTION CLOSED
    connection.close()

def create_table():
    # database connectivity
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="urpassword",
        database="lib"
    )

    # CREATE TABLE FOR BOOKS
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), category VARCHAR(255))")
    print("TABLE CREATED SUCCESFULLY!")

    # CONNECTION CLOSED
    connection.close()

def add_book():
    # DATABASE CONNECTION ESTABLISHED
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="urpassword",
        database="lib"
    )

    # Get book details from user
    title = input("enter the book title: ")
    author = input("author name: ")
    category = input("enter the book category: ")

    # Insert book details into the table
    cursor = connection.cursor()
    query = "INSERT INTO books (title, author, category) VALUES (%s, %s, %s)"
    values = (title, author, category)
    cursor.execute(query, values)
    connection.commit()
    print("book adds successfully!")

    # connection closed
    connection.close()

def view_books():
    # connection established
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="urpassword",
        database="lib"
    )

    # Retrieve books from the book details table

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    if len(books) == 0:
        print("no book found।")
    else:
        print("book details:")
        for book in books:
            print("ID:", book[0])
            print("book title:", book[1])
            print("authors name:", book[2])
            print("books category:", book[3])
            print("---------------------")

    # connection established
    connection.close()

def main():
    create_database()
    create_table()

    while True:
        print("\nlibrary management system")
        print("1. add books")
        print("2. see books")
        print("3. exit")

        choice = input("select (1-3): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            print("exit...")
            break
        else:
            print("invalid option... try again।")

if __name__ == '__main__':
    main()
