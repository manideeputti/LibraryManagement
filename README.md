# Library Management System

## Overview
This project is a Flask-based Library Management System that allows users to manage books and members in a library. The system supports functionalities such as adding, retrieving, and deleting books and members, as well as searching for books by title or author.

## Features
1. **Book Management**:
   - Add a new book.
   - Retrieve details of a specific book by its ID.
   - Delete a book.
   - Search books by title or author.

2. **Member Management**:
   - Add a new member.
   - Retrieve a list of all members.

## Prerequisites
- Python 3.7 or above
- Flask

## Installation
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd library-management-system
   ```

2. **Set Up Virtual Environment** (Optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Project Structure**:
   - `app.py`: Main application file.
   - `models.py`: Contains class definitions for `Book` and `Member`.
   - `Database.py`: Mock database storing `Books` and `Members`.
   - `requirements.txt`: Python dependencies.

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the Application**:
   Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

## API Endpoints
### Books
- **Add a Book**: `POST /Books`
  - Request Body:
    ```json
    {
        "Book_name": "Book Title",
        "Author": "Author Name"
    }
    ```
  - Response:
    ```json
    {
        "message": "Book added successfully"
    }
    ```

- **Get a Book**: `GET /Books/<book_id>`
  - Response:
    ```json
    {
        "Book_id": 1,
        "Book_name": "Book Title",
        "Author": "Author Name",
        "availability": true
    }
    ```

- **Update a Book**: `PUT /Books/<book_id>`
  - Request Body:
    ```json
    {
        "Book_name": "Updated Title",
        "Author": "Updated Author"
    }
    ```
  - Response:
    ```json
    {
        "message": "Book updated successfully"
    }
    ```

- **Delete a Book**: `DELETE /Books/<book_id>`
  - Response:
    ```json
    {
        "message": "Book deleted successfully"
    }
    ```

- **Search Books**: `GET /Books/Search`
  - Request Body:
    ```json
    {
        "query": "Search Query"
    }
    ```
  - Response:
    ```json
    [
        {
            "Book_id": 1,
            "Book_name": "Book Title",
            "Author": "Author Name",
            "availability": true
        }
    ]
    ```

### Members
- **Add a Member**: `POST /Members`
  - Request Body:
    ```json
    {
        "Name": "Member Name",
        "Age": 25,
        "Gender": "M"
    }
    ```
  - Response:
    ```json
    {
        "message": "Member added successfully"
    }
    ```

- **Get All Members**: `GET /Members`
  - Response:
    ```json
    [
        {
            "Id": 1,
            "Name": "Member Name",
            "Age": 25,
            "Gender": "M"
        }
    ]
    ```

## Mock Database
- The application uses an in-memory list (`Books` and `Members`) to store data.
- Replace this with a persistent database (e.g., SQLite, PostgreSQL) for production use.

## Contribution
1. Fork the repository.
2. Create a new branch for your feature/fix.
3. Submit a pull request with a detailed description of your changes.

## Contact
For questions or feedback, please contact [umdn1030@gmail.com].

