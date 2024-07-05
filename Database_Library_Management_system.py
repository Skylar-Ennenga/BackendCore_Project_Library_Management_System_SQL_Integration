from user_data import add_user, view_user_details, display_all_users
from book_data import add_book, display_all_books, check_out_book, return_book, search_book_by
from author_data import add_author, view_author_details, display_all_authors
from connect_my_sql import connect_db
from mysql.connector import Error
import re

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
                choice = input("Before you add a book you will need the Authors ID#. Would you like to continue? \nYes or No\n").lower()
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
