CREATE DATABASE library_management_db;

USE library_management_db;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    genre_id INT,
    isbn VARCHAR(13) NOT NULL,
    publication_date DATE,
    availability BOOLEAN DEFAULT 1,
    FOREIGN KEY (author_id) REFERENCES authors(id)    
);

CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    library_id VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);


ALTER TABLE users
ADD phone VARCHAR(15); -- adds a column called phone to the Customers table

ALTER TABLE users
add email VARCHAR(200);

ALTER TABLE books
DROP COLUMN genre_id;

ALTER TABLE books
ADD genre VARCHAR(255);


SELECT * FROM borrowed_books;
SELECT * FROM books;

UPDATE books
SET title = "The Lord of the Rings: The Fellowship of the Ring"
WHERE id = 1;

-- Insert authors
INSERT INTO authors (id, name, biography) VALUES

(7, 'Agatha Christie', 'Author of Hercule Poirot and Miss Marple series.'),
(8, 'Jane Austen', 'Author of Pride and Prejudice.'),
(9, 'Arthur Conan Doyle', 'Author of Sherlock Holmes series.'),
(10, 'Nicholas Sparks', 'Author of The Notebook.');



INSERT INTO books (id, title, author_id, genre, isbn, publication_date, availability) VALUES

(15, 'Murder on the Orient Express', 7, 'Mystery', '9780062073501', '1934-01-01', 1),
(16, 'Pride and Prejudice', 8, 'Romance', '9780141040349', '1813-01-28', 1),
(17, 'The Hound of the Baskervilles', 9, 'Mystery', '9780451528018', '1902-04-01', 1),
(18, 'The Notebook', 10, 'Romance', '9780446605236', '1996-10-01', 1);


-- Insert books by Brandon Sanderson
INSERT INTO books (title, author_id, genre, isbn, publication_date, availability) VALUES
('The Final Empire', 2, 'Fantasy', '9780765311788', '2006-07-25', 1),
('The Well of Ascension', 2, 'Fantasy', '9780765316882', '2007-08-21', 1),
('The Hero of Ages', 2, 'Fantasy', '9780765316899', '2008-10-14', 1),
('Warbreaker', 2, 'Fantasy', '9780765320308', '2009-06-09', 1),
('The Way of Kings', 2, 'Fantasy', '9780765326355', '2010-08-31', 1),
('Words of Radiance', 2, 'Fantasy', '9780765326362', '2014-03-04', 1),
('Oathbringer', 2, 'Fantasy', '9780765326379', '2017-11-14', 1),
('Rhythm of War', 2, 'Fantasy', '9780765326386', '2020-11-17', 1);

-- Insert users
-- Insert users with random 4-digit library IDs
INSERT INTO users (name, library_id, email, phone) VALUES
('Gandalf the Grey', '1234', 'gandalf@middleearth.com', '555-1234'),
('Frodo Baggins', '5678', 'frodo@shire.me', '555-5678'),
('Hermione Granger', '8765', 'hermione@hogwarts.edu', '555-8765'),
('Jon Snow', '4321', 'jonsnow@nightwatch.org', '555-4321'),
('Aragorn son of Arathorn', '3456', 'aragorn@gondor.gov', '555-3456'),
('Legolas Greenleaf', '6789', 'legolas@woodlandrealm.el', '555-6789'),
('Tyrion Lannister', '9876', 'tyrion@casterlyrock.lan', '555-9876'),
('Harry Potter', '5432', 'harry@hogwarts.edu', '555-5432'),
('Daenerys Targaryen', '6543', 'daenerys@drakaris.com', '555-6543'),
('Bilbo Baggins', '7654', 'bilbo@shire.me', '555-7654');





