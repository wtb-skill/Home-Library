# Project Title

Home Library Management System

## Overview

The Home Library Management System is a Flask-based application that allows users to manage their personal book collection. It provides a web interface for adding, viewing, and updating book details, as well as an API for programmatic access.

## Prerequisites

    Python 3.x
    Flask
    (For API) cURL or a tool to make HTTP requests

## Installation

    Clone the repository:

    bash

    git clone https://github.com/wtb-skill/Home-Library.git

    Navigate to the project directory:
    
    bash
    
    cd Home-Library(flask)
    
    Install dependencies:
    
    bash

    pip install -r requirements.txt

## Getting Started

    Run the application:

    bash

    python app.py

    Access the web interface:
    Open your browser and go to http://127.0.0.1:5000/

## Usage

    Adding a Book:
        Navigate to http://127.0.0.1:5000/books/add/
        or click 'Add new book' in the browser
        Fill in the book details and submit the form.

    Viewing Library:
        Navigate to http://127.0.0.1:5000/books/
        or click 'Display and edit' in the browser
        View all books in the library.

    Sorting Library:
        Sort books by title: http://127.0.0.1:5000/books/?sort=title
        Sort books by author: http://127.0.0.1:5000/books/?sort=author
        Sort books by read status: http://127.0.0.1:5000/books/?sort=read
        or click 'Title', 'Author' or 'Read' in the display part of the site.

    Viewing a Book:
        Navigate to http://127.0.0.1:5000/books/<int:book_id>/
        or click on a book title 
        View and/or edit the book's details.

    Get a random unread book:
        Navigate to http://127.0.0.1:5000/choose_unread_book/
        Get a randomly chosen unread book.

## Project Structure

- **app.py**: Main application file containing the Flask app.
- **api_routes.py**: Rest API routes for book management.
- **models.py**: Model for handling books for the web interface and the API.
- **forms.py**: Flask-WTF forms for book-related forms.
- **config.py**: Contains config settings.
- **books.json**: Contains books data in json format.
- **README.md**: This file.
- **requirements.txt**: Helps in managing project dependencies and allows for easy installation of the required packages.
- **templates/**
  - **base.html**: The base template for other HTML files.
  - **add_book.html**: Template for adding a new book.
  - **display.html**: Template for displaying books.
  - **edit.html**: Template for editing book details.
  - **menu.html**: Template for the main menu.
- **static/**
  - **menu_books.jpeg**: Image file.
  - **open_book.jpg**: Image file.
  - **style.css**: CSS stylesheet file.

The project is organized into different components, each serving a specific purpose. Key files and directories are listed above to help you navigate through the codebase.


## Configuration

The application is configured using the config.py file. 

## API Documentation:

    List all books:
        Endpoint: http://127.0.0.1:5000/api/v1/books/
        Method: GET
        Response: JSON array of all books.

    Get a book by ID:
        Endpoint: http://127.0.0.1:5000/api/v1/books/{book_id}
        Method: GET
        Response: JSON object representing the book.

    Get a random unread book:
        Endpoint: http://127.0.0.1:5000/api/v1/choose_unread_book/
        Method: GET
        Response: JSON object representing a random unread book.

    Create a new book:
        Endpoint: http://127.0.0.1:5000/api/v1/books/
        Method: POST
        Request: JSON object with book details.
        Response: JSON object representing the created book.

    Delete a book by ID:
        Endpoint: http://127.0.0.1:5000/api/v1/books/{book_id}
        Method: DELETE
        Response: JSON object with the result.

    Update a book by ID:
        Endpoint: http://127.0.0.1:5000/api/v1/books/{book_id}
        Method: PUT
        Request: JSON object with updated book details.
        Response: JSON object representing the updated book.

## Note:

    This README assumes default configuration settings.
    For API testing, you can use tools like cURL or Postman.
    Make sure to populate books.json with initial data if not present.

## Authors

    Adam Bałdyga

## License

This project is licensed under the MIT License.