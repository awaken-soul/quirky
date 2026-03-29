from fastapi import FastAPI
from routes import router as BookRouter

app = FastAPI(title="Personal Book Library API")

# Fix the 404 error at "/"
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Book Library API! Go to /docs for Swagger."}

# Include all the routes from routes.py
app.include_router(BookRouter, tags=["Books"], prefix="/books")