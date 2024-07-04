from connect_my_sql import connect_db
from mysql.connector import Error
import random
from datetime import date



def add_book():    
    try:
        conn = connect_db()
        cursor = conn.cursor()

        print("Welcome to adding a book\n")
        title = input("Please enter the Book Title: ")
        author_id = int(input("Please enter the Book Author: "))
        genre = input("Please enter the Book Genre: ")
        isbn = str(random.randint(1000000000000, 9999999999999))
        pub_date = input("Please enter the Book Publication Date: (YYYY-MM-DD) ")

        new_book = (title, author_id, genre, isbn, pub_date)

        # query to insert order
        query = "INSERT INTO books(title, author_id, genre, isbn, publication_date) VALUES (%s, %s, %s, %s, %s)"

    # Executing query and committing changes

        # executing query and committing changes
        cursor.execute(query, new_book)
        
        conn.commit()
        print("Book has been added successfully")
 
        
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
            conn.close() #turns of the connection to the db
#add_book()

def view_book_details():
    
    try:
        conn = connect_db()
        cursor = conn.cursor()

        book_name = input("Enter the name of the book you would like to see ")
        
        # create a SQL query as a python string
        query = """
        SELECT books.title, authors.name, books.genre, books.publication_date, books.availability, books.id 
        FROM books
        JOIN authors ON books.author_id = authors.id
        WHERE books.title = %s
        """ 
        # Executing the query using the cursor
        cursor.execute(query, (book_name,))

        records = cursor.fetchall()

        if not records:
            print("No book found with that title.")
            return

        # Loop through the results and print each row of data
        for row in records:
            if row[4] == 1:
                print(f"\nTitle: {row[0]} \nAuthor: {row[1]} \nGenre: {row[2]} \nPublication Date: {row[3]} \nAvailibility: Availible \nCheckout ID# {row[5]}\n")

            elif row[4] == 0:
                print(f"\nTitle: {row[0]} Author: {row[1]} Genre: {row[2]} Publication Date: {row[3]} Availibility: Borrowed \nCheckout ID# {row[5]}\n")
    
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
            conn.close() #turns of the connection to the db
#view_book_details()

def display_all_books():
    
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # create a SQL query as a python string
        query = """
                SELECT books.title, authors.name, books.genre, books.publication_date, books.availability, books.id
                FROM books
                JOIN authors ON books.author_id = authors.id;

        """
        # Executing the query using the cursor
        cursor.execute(query)

        records = cursor.fetchall()
        
        for row in records:
            if row[4] == 1:
                print(f"\nTitle: {row[0]} \nAuthor: {row[1]} \nGenre: {row[2]} \nPublication Date: {row[3]} \nAvailibility: Availible \nCheckout ID# {row[5]}\n")

            elif row[4] == 0:
                print(f"\nTitle: {row[0]} \nAuthor: {row[1]} \nGenre: {row[2]} \nPublication Date: {row[3]} \nAvailibility: Borrowed \nCheckout ID# {row[5]}\n")
                

 
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
            conn.close() #turns of the connection to the db
#display_all_books()  

def check_out_book():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        user_id = int(input("Enter your user ID: "))
        book_id = int(input("Enter the book ID to borrow: "))

        query = "SELECT availability FROM books WHERE id = %s"
        # Check if the book is available
        cursor.execute(query, (book_id,))
        
        available = cursor.fetchone()[0]

        if not available:
            print("Sorry, this book is not available.")
            return

        # Insert into borrowed_books
        borrow_date = date.today()
       
        query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
        
        
        cursor.execute(query, (user_id, book_id, borrow_date))

        query1 = ("UPDATE books SET availability = 0 WHERE id = %s")
        # Update book availability
        cursor.execute(query1, (book_id,))

        conn.commit()
        print("Book has been borrowed successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
#check_out_book()

def return_book ():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        user_id = int(input("Enter your user ID: "))
        book_id = int(input("Enter the book ID to return: "))

        
        return_date = date.today() # Update return_date in borrowed_books
        query = "UPDATE borrowed_books SET return_date = %s WHERE user_id = %s AND book_id = %s AND return_date IS NULL"  # Update the return date where the user_id and book_id match and the return date is null this will prevent the user from returning the same book twice
        cursor.execute(query, (return_date, user_id, book_id)) # Execute the query with the return date, user_id, and book_id 

        if cursor.rowcount == 0: # If the row count is 0 then the book was not borrowed by the user
            print("No borrowed record found for this book and user.")
            return

        query1 = "UPDATE books SET availability = 1 WHERE id = %s"
        # Update book availability
        cursor.execute(query1, (book_id,))

        conn.commit()
        print("Book has been returned successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
#return_book()

def search_book_by():
    while True:
        try:
            user_input = int(input("What would you like to search by? \n1. Title \n2. Author \n3. Genre \n4. Book ID# \n5. Go Back\n"))
            if user_input == 1:
                try:
                    conn = connect_db()
                    cursor = conn.cursor()

                    book_name = input("Enter the name of the book you would like to see ")
                    
                    # create a SQL query as a python string
                    query = """
                    SELECT books.title, authors.name, books.genre, books.publication_date, books.availability, books.id 
                    FROM books
                    JOIN authors ON books.author_id = authors.id
                    WHERE books.title = %s
                    """ 
                    # Executing the query using the cursor
                    cursor.execute(query, (book_name,))

                    records = cursor.fetchall()

                    if not records:
                        print("No book found with that title.")
                        return

                    # Loop through the results and print each row of data
                    for row in records:
                        if row[4] == 1:
                            print(f"\nTitle: {row[0]} Author: {row[1]} Genre: {row[2]} Publication Date: {row[3]} \nAvailibility: Availible \nCheckout ID# {row[5]}\n")

                        elif row[4] == 0:
                            print(f"\nTitle: {row[0]} Author: {row[1]} Genre: {row[2]} Publication Date: {row[3]} \nAvailibility: Borrowed \nCheckout ID# {row[5]}\n")
                
                except Error as e:
                    print(f"Error: {e}")

                finally:
                    if conn and conn.is_connected():
                        cursor.close() #turns off the cursor
                        conn.close() #turns of the connection to the db
            elif user_input == 2:
                try:
                    conn = connect_db()
                    cursor = conn.cursor()

                    author_name = input("Enter the name of the author you would like to see ")
                    
                    # create a SQL query as a python string
                    query = """
                    SELECT books.title, authors.name, books.genre, books.publication_date, books.availability, books.id 
                    FROM books
                    JOIN authors ON books.author_id = authors.id
                    WHERE authors.name = %s
                    """ 
                    # Executing the query using the cursor
                    cursor.execute(query, (author_name,))

                    records = cursor.fetchall()

                    if not records:
                        print("No book found with that author.")
                        return

                    # Loop through the results and print each row of data
                    for row in records:
                        if row[4] == 1:
                            print(f"\nTitle: {row[0]} Author: {row[1]} Genre: {row[2]} Publication Date: {row[3]} \nAvailibility: Availible \nCheckout ID# {row[5]}\n")

                        elif row[4] == 0:
                            print(f"\nTitle: {row[0]} Author: {row[1]} Genre: {row[2]} Publication Date: {row[3]} \nAvailibility: Borrowed \nCheckout ID# {row[5]}\n")
                
                except Error as e:
                    print(f"Error: {e}")

                finally:
                    if conn and conn.is_connected():
                        cursor.close()
            elif user_input == 3:
                try:
                    conn = connect_db()
                    cursor = conn.cursor()

                    genre = input("Enter the genre of the book you would like to see ")
                    
                    # create a SQL query as a python string
                    query = """
                    SELECT books.title, authors.name, books.genre, books.publication_date, books.availability, books.id 
                    FROM books
                    JOIN authors ON books.author_id = authors.id
                    WHERE books.genre = %s
                    """ 
                    # Executing the query using the cursor
                    cursor.execute(query, (genre,))

                    records = cursor.fetchall()

                    if not records:
                        print("No book found with that genre.")
                        return

                    # Loop through the results and print each row of data
                    for row in records:
                        if row[4] == 1:
                            print(f"\nTitle: {row[0]} Author: {row[1]} Genre: {row[2]} Publication Date: {row[3]} \nAvailibility: Availible \nCheckout ID# {row[5]}\n")

                        elif row[4] == 0:
                            print(f"\nTitle: {row[0]} Author: {row[1]} Genre: {row[2]} Publication Date: {row[3]} \nAvailibility: Borrowed \nCheckout ID# {row[5]}\n")
                
                except Error as e:
                    print(f"Error: {e}")

                finally:
                    if conn and conn.is_connected():
                        cursor.close()
            elif user_input == 4:
                try:
                    conn = connect_db()
                    cursor = conn.cursor()

                    book_id = int(input("Enter the ID# of the book you would like to see "))
                    
                    # create a SQL query as a python string
                    query = """
                    SELECT books.title, authors.name, books.genre, books.publication_date, books.availability, books.id 
                    FROM books
                    JOIN authors ON books.author_id = authors.id
                    WHERE books.id = %s
                    """ 
                    # Executing the query using the cursor
                    cursor.execute(query, (book_id,))

                    records = cursor.fetchall()

                    if not records:
                        print("No book found with that ID#.")
                        return

                    # Loop through the results and print each row of data
                    for row in records:
                        if row[4] == 1:
                            print(f"\nTitle: {row[0]} Author: {row[1]} Genre: {row[2]} Publication Date: {row[3]} \nAvailibility: Availible \nCheckout ID# {row[5]}\n")

                        elif row[4] == 0:
                            print(f"\nTitle: {row[0]} Author: {row[1]} Genre: {row[2]} Publication Date: {row[3]} \nAvailibility: Borrowed \nCheckout ID# {row[5]}\n")
                
                except Error as e:
                    print(f"Error: {e}")

                finally:
                    if conn and conn.is_connected():
                        cursor.close()
            elif user_input == 5:
                break
            else:
                print("Please choose a number between 1-4")
        
        except ValueError:
            print("Thats not a number! PLease choose a number between 1-4")

#search_book_by()

