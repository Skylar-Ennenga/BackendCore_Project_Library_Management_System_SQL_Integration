from user_data import add_user, view_user_details, display_all_users
from book_data import add_book, view_book_details, display_all_books, check_out_book, return_book, search_book_by
from author_data import add_author, view_author_details, display_all_authors
from connect_my_sql import connect_db
from mysql.connector import Error
import re

    # Establish a connection to the MySQL database using the mysql-connector-python library.

    # Create a database cursor to execute SQL queries. Functions for Data Manipulation:

    # Create functions for adding new books, users, authors, and genres to the database.

    # Implement functions for updating book availability, marking books as borrowed or returned.

    # Develop functions for searching books by book_id, title, author, or genre.

    # Define functions for displaying lists of books, users, authors

    # Implement functions for user registration and viewing user details. User Interface Functions:

    # Create a user-friendly command-line interface (CLI) with clear menu options.

    # Implement functions to handle user interactions using the input() function.

    # Validate user input using regular expressions (regex) to ensure proper formatting. Error Handling:

    # Use try, except, else, and finally blocks to manage errors gracefully.

    # Handle exceptions related to database operations, input validation, and other potential issues.

    # Provide informative error messages to guide users. Clean Code Principles:

    # Use meaningful variable and function names that convey their purpose.

    # Write clear comments and docstrings to explain the functionality of functions and classes.

    # Follow PEP 8 style guidelines for code formatting and structure.

    # Ensure proper indentation and spacing for readability. Modular Design:

    # Organize code into separate modules to promote modularity and maintainability.

    # Create distinct modules for database operations, user interactions, error handling, and core functionalities. GitHub Repository:

    # Create a GitHub repository for your project and commit code regularly.

    # Maintain a clean and interactive README.md file in your GitHub repository, providing clear instructions on how to run the application and explanations of its features.







def main(): # Main function to run the program
    while True:
        print("\nWelcome to the Library Management System!\n")
        try:
            main_menu_choice = int(input("Main Menu:\n1. Book Operations \n2. User Operations \n3. Author Operations\n4. Quit\n"))
            if main_menu_choice == 1:
                book_main() # Calls the book_main function
            elif main_menu_choice == 2:
                user_main() # Calls the user_main function
            elif main_menu_choice == 3:
                author_main() # Calls the author_main function
            elif main_menu_choice == 4:
                break
            else:
                print("\nPlease choose a number between 1-4\n")
        except ValueError: # If the user enters a letter instead of a number
            print("\nThats not a number! PLease choose a number between 1-4\n")


def book_main(): # Function to run the book operations
    while True:
        try:
            book_menu_choice = int(input("\nBook Operations: \n1. Add a new book \n2. Checkout a book \n3. Return a book \n4. Search for a book \n5. Display all books \n6. Return to Main Menu \n"))
            if book_menu_choice == 1:
                choice = input("Before you add a book you will need the Authors ID# of the Author of the book. Would you like to continue? \nYes or No\n").lower()
                if choice == "yes":
                    add_book()
                else:
                    pass
            elif book_menu_choice == 2:
                check_out_book()
                pass
            elif book_menu_choice == 3:
                return_book()
                pass
            elif book_menu_choice == 4:
                search_book_by()
                pass
            elif book_menu_choice == 5:
                display_all_books()
            elif book_menu_choice == 6:
                break
            else:
                print("\nPlease choose a number between 1-6\n")
        except ValueError:
            print("\nThats not a number! PLease choose a number between 1-6\n")

def verify_email(email):
    pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}") # Define the regex pattern for email
    if re.match(pattern, email): # Check if the email matches the pattern
        return True
    else:
        return False



def user_main(): # Function to run the user operations
    while True:
        try:
            book_menu_choice = int(input("\nUser Operations: \n1. Add a new user \n2. View user details \n3. Display all users \n4. Return to Main Menu \n"))
            if book_menu_choice == 1:
                add_user()
            elif book_menu_choice == 2:
                view_user_details()
            elif book_menu_choice == 3:
                display_all_users()
            elif book_menu_choice == 4:
                break
            else:
                print("\nPlease choose a number between 1-4\n")
        except ValueError:
            print("\nThats not a number! PLease choose a number between 1-4\n")


def author_main(): # Function to run the author operations
    while True:
        try:
            book_menu_choice = int(input("\nAuthor Operations: \n1. Add a new author \n2. View author details \n3. Display all authors \n4. Return to Main Menu \n"))
            if book_menu_choice == 1:
                add_author()
            elif book_menu_choice == 2:
                view_author_details()
            elif book_menu_choice == 3:
                display_all_authors()
            elif book_menu_choice == 4:
                break
            else:
                print("\nPlease choose a number between 1-4\n")
        except ValueError:
            print("\nThats not a number! PLease choose a number between 1-4\n")

if __name__ == "__main__":
    main()
