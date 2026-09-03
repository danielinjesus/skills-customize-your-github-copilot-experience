# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework, including defining routes, validating data with Pydantic models, and handling CRUD operations.

## 📝 Tasks

### 🛠️	Set Up a Basic FastAPI App

#### Description
Using the provided starter code, create a FastAPI application with a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Define a `GET /` endpoint that returns a JSON message like `{"message": "Welcome to the Book API"}`
- Run successfully with `uvicorn` and be viewable in the interactive docs at `/docs`

### 🛠️	Create a Data Model with Pydantic

#### Description
Define a Pydantic model named `Book` to represent a book's data, and use it to validate incoming request data.

#### Requirements
Completed program should:

- Define a `Book` model with fields `title` (str), `author` (str), and `year` (int)
- Store books in an in-memory list
- Define a `POST /books` endpoint that accepts a `Book` and adds it to the list

### 🛠️	Build CRUD Endpoints

#### Description
Add endpoints to retrieve all books, retrieve a single book by its position in the list, and delete a book.

#### Requirements
Completed program should:

- Define a `GET /books` endpoint that returns the full list of books
- Define a `GET /books/{book_id}` endpoint that returns a single book by index
- Define a `DELETE /books/{book_id}` endpoint that removes a book by index
- Return a `404` error with a clear message when `book_id` does not exist

### 🛠️	Add Input Validation and Error Handling (Stretch Goal)

#### Description
Improve the API by validating input more strictly and returning helpful error responses.

#### Requirements
Completed program should:

- Ensure `year` must be a reasonable value (e.g., greater than 1450, the year of the printing press)
- Return a `400` error with a descriptive message when validation fails
- Add a `PUT /books/{book_id}` endpoint to update an existing book's details
