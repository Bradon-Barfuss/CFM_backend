from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import csv
import os
import hashlib

app = FastAPI()

CSV_FILE = "users.csv"

from fastapi.middleware.cors import CORSMiddleware

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your React app URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create CSV file if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password_hash"])  # Header row

# Pydantic model for request body
class LoginRequest(BaseModel):
    username: str
    password: str

# Read users from CSV
def read_users():
    users = {}
    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            users[row[0]] = row[1]  # Store {username: password_hash}
    return users

# API to handle login and register
@app.post("/login")
async def login(request: LoginRequest):
    users = read_users()

    # Check if user already exists
    if request.username in users:
        return {"message": "User already exists"}

    # Write new user to CSV file
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([request.username, request.password])  # ⚠️ Hash password in real-world apps

    return {"message": "User registered successfully"}
