from connect_my_sql import connect_db
from mysql.connector import Error
import random





def add_user():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # collect customer information to add to the database
        name = input("Please enter the customer's name: ")
        email = input("Please enter the customer's email: ")
        phone = input("Please enter the customer's phone number" )
        library_id = random.randint(1000, 9999)

        # creating the tuple that we will send over to the database
        # we set this to a tuple becuase the execute query method needs an iterable to match the position of values
        new_user = (name, email, phone, library_id)

        # SQL Query to insert customer information                  place holders for the data to be inserted
        query = "INSERT INTO Users (name, email, phone, library_id) VALUES (%s, %s, %s, %s)"

        # excecute the query
        cursor.execute(query, new_user) #prepares query with arguments
        conn.commit() #commits and sends changes to our database
        print(f"{name} has successfully been added to the database!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close() 
#add_user()
def view_user_details():
    
    try:
        conn = connect_db()
        cursor = conn.cursor()
        
        user_id = input("Please iunput your 4 digit library ID: ")
        query = """ 
        SELECT users.id, users.name, users.email, users.phone, books.title, borrowed_books.borrow_date, borrowed_books.return_date
        FROM users
        LEFT JOIN borrowed_books ON users.id = borrowed_books.user_id AND borrowed_books.return_date IS NULL 
        LEFT JOIN books ON borrowed_books.book_id = books.id
        WHERE users.id = %s;
        """
        # Executing the query using the cursor
        cursor.execute(query, (user_id,))
        
        records = cursor.fetchall()

        if not records:
            print(f"No user found with ID: {user_id}")
            return
    
        print(records)
        #Since the query returns the full query for each book instance we take the user info from the first instance
        user_info = {
            'id': records[0][0],
            'name': records[0][1],
            'email': records[0][2],
            'phone': records[0][3],
            'books': []
        }
         # Then we iterate through each instance to grab the name of the book 
        for record in records:
            book_title = record[4]
            borrow_date = record[5]
            return_date = record[6]

            if book_title:
                user_info['books'].append({
                    'title': book_title,
                    'borrow_date': borrow_date,
                    'return_date': return_date if return_date else 'Not Returned'
                })

        # Print user information 
        print(f"\nUser ID: {user_info['id']}")
        print(f"User Name: {user_info['name']}")
        print(f"User Email: {user_info['email']}")
        print(f"User Phone: {user_info['phone']}")

        if user_info['books']: #if the user has books borrowed we print them
            print("Currently Borrowed Books:")
            for book in user_info['books']:
                print(f"  - Title: {book['title']}")
                print(f"    Borrow Date: {book['borrow_date']}")
                print(f"    Return Date: {book['return_date']}")
        else:
            print("Currently Borrowed Books: None") # if the user has no books borrowed we print this
          
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
            conn.close() #turns of the connection to the db
#view_user_details()

def display_all_users():
    
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # create a SQL query as a python string
        query = "SELECT * FROM Users"

        # Executing the query using the cursor
        cursor.execute(query)

        # fetching the results from the above query
        # print(cursor.fetchall())
        # loops through the results and prints each row of data
        # is returned as an tuple
        for row in cursor.fetchall():#fetchall returns data from the query execution as a list of tuples
            # looping through the list of tuples
            print(f"\nUser ID# {row[0]} \nName: {row[1]}\nLibrary ID# {row[2]}\nPhone: {row[3]}\nEmail: {row[4]}\n")
    
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
            conn.close() #turns of the connection to the db

#display_all_users()
