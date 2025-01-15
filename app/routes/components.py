from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Data model for a component
class Component(BaseModel):
    id: str
    type: str  # e.g., "context" or "verse"
    content: str  # Optional: Add this if you want to save user input

# In-memory database to store components (replace with a real DB later)
db = []

# Fetch all components
@router.get("/", response_model=List[Component])
def get_components():
    return db

# Save/update components
@router.post("/")
def save_components(components: List[Component]):
    global db
    db = components  # Replace the entire state with the new one
    return {"message": "Components saved successfully!"}

@router.delete("/{id}")
def delete_component(id: str):
    global db
    db = [component for component in db if component.id != id]
    return {"message": "Component deleted successfully!"}

