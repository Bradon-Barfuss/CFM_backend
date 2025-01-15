from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import components

app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your React app URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(components.router, prefix="/components")
