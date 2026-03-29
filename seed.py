from database import book_collection
from datetime import datetime

# Sample data to populate your library
sample_books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "genre": "Classic",
        "is_read": True
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "genre": "Dystopian",
        "is_read": False
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "genre": "Fantasy",
        "is_read": True
    },
    {
        "title": "Project Hail Mary",
        "author": "Andy Weir",
        "year": 2021,
        "genre": "Sci-Fi",
        "is_read": False
    },
    {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008,
        "genre": "Education",
        "is_read": True
    }
]

def seed_database():
    try:
        # Clear existing data so you don't get duplicates every time you run this
        book_collection.delete_many({})
        print("Database cleared.")

        # Bulk insert
        result = book_collection.insert_many(sample_books)
        print(f"Successfully inserted {len(result.inserted_ids)} books!")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    seed_database()
