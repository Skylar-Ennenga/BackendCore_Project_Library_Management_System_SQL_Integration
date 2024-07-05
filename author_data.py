from connect_my_sql import connect_db
from mysql.connector import Error


def add_author():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # collect customer information to add to the database
        author_name = input("Please enter the name of the Author you would like to add: ")
        author_bio = input(f"Please input a short bio for {author_name} ")
    
       

        # creating the tuple that we will send over to the database
        # we set this to a tuple becuase the execute query method needs an iterable to match the position of values
        new_author = (author_name, author_bio)

        # SQL Query to insert customer information                  place holders for the data to be inserted
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"

        # excecute the query
        cursor.execute(query, new_author) #prepares query with arguments
        conn.commit() #commits and sends changes to our database
        print(f"{author_name} has successfully been added to the database!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close() 
#add_author()

def view_author_details():
    
    try:
        conn = connect_db()
        cursor = conn.cursor()

        author_id = input("Enter the Author ID# ")
        
        # create a SQL query as a python string
        query = "SELECT * FROM authors WHERE id = %s" # Make specific string

        # Executing the query using the cursor
        cursor.execute(query, (author_id,))
        
        records = cursor.fetchall()
        # fetching the results from the above query
        # print(cursor.fetchall())
        # loops through the results and prints each row of data
        # is returned as an tuple
        for row in records:#fetchall returns data from the query execution as a list of tuples
            # looping through the list of tuples
            print(f"Author ID# {row[0]} \nName: {row[1]}\nBiography: \n{row[2]}")
    
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
            conn.close() #turns of the connection to the db
#view_author_details()

def display_all_authors():
    
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Went with a left join so it would still show the authors even if they didnt have a book assigned to them
        query = """ SELECT authors.id, authors.name, books.title
                    FROM authors
                    LEFT JOIN books ON authors.id = books.author_id; 
                """

        # Executing the query using the cursor
        cursor.execute(query)

        records = cursor.fetchall()
        
        if not records:
            print("No records found.")
            return
        
        authors_books = {}
        # ended up adding all this information back to a dictionary so i could disply like i did in my previous project
        for row in records:
            author_id = row[0]
            author_name = row[1]
            book_title = row[2]

            if author_id not in authors_books:
                authors_books[author_id] = {'name': author_name, 'books': []} #creates a dictionary with the author id as the key and the name and books as the values
            
            if book_title:
                authors_books[author_id]['books'].append(book_title) #appends the book title to the books list in the dictionary
        
        for author_id, author_name in authors_books.items(): #loops through the dictionary and prints the information
            print(f"\nAuthor ID: {author_id}")
            print(f"Author: {author_name['name']}")
            if author_name['books']:
                print("Books:")
                for book_info in author_name['books']:
                    print(f"  - {book_info}")
            else:
                print("Books: Uh oh its empty time to add some books!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
            conn.close() #turns of the connection to the db
#display_all_authors()