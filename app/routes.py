from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from typing import Optional, List

# Use 'import' if files are in the same folder
# Use 'from .database' if they are in a sub-folder called 'app'
from database import book_collection, book_helper
from models import BookSchema, UpdateBookModel

router = APIRouter()

@router.post("/", response_description="Add new book", status_code=201)
async def add_book(book: BookSchema = Body(...)):
    book_data = jsonable_encoder(book)
    new_book = book_collection.insert_one(book_data)
    created_book = book_collection.find_one({"_id": new_book.inserted_id})
    return book_helper(created_book)

@router.get("/", response_description="List all books")
async def get_books(genre: Optional[str] = None):
    query = {}
    if genre:
        query = {"genre": genre}
    books = [book_helper(book) for book in book_collection.find(query)]
    return books

@router.get("/{id}", response_description="Get a single book")
async def show_book(id: str):
    # Ensure the ID is a valid MongoDB ObjectId before searching
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
        
    if (book := book_collection.find_one({"_id": ObjectId(id)})) is not None:
        return book_helper(book)
    raise HTTPException(status_code=404, detail=f"Book {id} not found")

@router.put("/{id}", response_description="Update a book")
async def update_book(id: str, req: UpdateBookModel = Body(...)):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    # .dict() is for Pydantic v1, .model_dump() is for Pydantic v2
    # We filter out None values so we don't overwrite data with nulls
    update_data = {k: v for k, v in req.model_dump().items() if v is not None}
    
    if len(update_data) >= 1:
        update_result = book_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": update_data}
        )
        if update_result.modified_count == 1:
            if (updated_book := book_collection.find_one({"_id": ObjectId(id)})) is not None:
                return book_helper(updated_book)
    
    if (existing_book := book_collection.find_one({"_id": ObjectId(id)})) is not None:
        return book_helper(existing_book)
        
    raise HTTPException(status_code=404, detail=f"Book {id} not found")

@router.delete("/{id}", response_description="Delete a book")
async def delete_book(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
        
    delete_result = book_collection.delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 1:
        return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Book {id} not found")