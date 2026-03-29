from pymongo import MongoClient
# Connection string (Use Environment Variables in a real production app)
MONGO_DETAILS = "mongodb+srv://admin:admin101@fastapi.69rjbxd.mongodb.net/?appName=Fastapi"

client = MongoClient(MONGO_DETAILS)
database = client.library_db
book_collection = database.get_collection("books_collection")

# Helper to convert MongoDB BSON to JSON-friendly Dictionary
def book_helper(book) -> dict:
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "year": book["year"],
        "genre": book["genre"],
        "is_read": book["is_read"],
    }