Here's a README for your Library Management System:

---

# Library Management System

## Introduction

Welcome to the Library Management System! This program allows users to manage a library's collection of books, authors, and user information. It provides functionalities to add, view, borrow, and return books, as well as manage user and author information.

## Features

- **Book Operations:**
  - Add a new book
  - Checkout a book
  - Return a book
  - Search for a book by title, author, genre, or book ID
  - Display all books

- **User Operations:**
  - Add a new user
  - View user details
  - Display all users

- **Author Operations:**
  - Add a new author
  - View author details
  - Display all authors

## Table of Contents

- [Library Management System](#library-management-system)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Table of Contents](#table-of-contents)
  - [Functions](#functions)
    - [Main Functions](#main-functions)
    - [Helper Functions](#helper-functions)
  - [Database Schema](#database-schema)
    - [Tables](#tables)
  - [Acknowledgements](#acknowledgements)

## Functions

### Main Functions

- `main()`: Main function to run the program, providing the main menu to choose between Book Operations, User Operations, Author Operations, and Quit.
- `book_main()`: Handles book-related operations.
- `user_main()`: Handles user-related operations.
- `author_main()`: Handles author-related operations.

### Helper Functions

- `verify_email(email)`: Validates email format using regex.
- `add_user()`: Adds a new user to the database.
- `view_user_details()`: Displays details of a specific user, including borrowed books.
- `display_all_users()`: Displays all users in the database.
- `verify_pub_date(pub_date)`: Validates publication date format using regex.
- `add_book()`: Adds a new book to the database.
- `display_all_books()`: Displays all books in the database.
- `check_out_book()`: Allows a user to borrow a book.
- `return_book()`: Allows a user to return a borrowed book.
- `search_book_by()`: Provides options to search for a book by title, author, genre, or book ID.

## Database Schema

### Tables

- `books`
  - `id` (INT, Primary Key)
  - `title` (VARCHAR)
  - `author_id` (INT, Foreign Key)
  - `genre` (VARCHAR)
  - `isbn` (VARCHAR)
  - `publication_date` (DATE)
  - `availability` (BOOLEAN)

- `authors`
  - `id` (INT, Primary Key)
  - `name` (VARCHAR)

- `users`
  - `id` (INT, Primary Key)
  - `name` (VARCHAR)
  - `email` (VARCHAR)
  - `phone` (VARCHAR)
  - `library_id` (INT)

- `borrowed_books`
  - `id` (INT, Primary Key)
  - `user_id` (INT, Foreign Key)
  - `book_id` (INT, Foreign Key)
  - `borrow_date` (DATE)
  - `return_date` (DATE)

## Acknowledgements

This project is a part of the Coding Temple Bootcamp. Special thanks to the instructors and fellow students for their support and guidance.

---

Feel free to customize this README further based on your specific project details and preferences.