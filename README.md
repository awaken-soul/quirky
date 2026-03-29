# Quirky
A CRUD API built with **FastAPI** and **MongoDB Atlas**.

## Features
- **Create**: Add books with automatic year validation.
- **Read**: Fetch all books or filter by genre.
- **Update**: Modify book details using MongoDB ObjectIDs.
- **Delete**: Remove books from the cloud database.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Start server: `uvicorn main:app --reload`
3. View Docs: `http://127.0.0.1:8000/docs`
