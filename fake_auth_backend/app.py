#  uvicorn app:app --reload

from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import jwt
from datetime import datetime

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Replace with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Secret key for JWT encoding/decoding
SECRET_KEY = "helloWorld"  # In production, use a secure secret key

# Define roles as strings
ROLES = ["Admin", "Doctor", "Nurse", "Radiologist", "LabTechnician", "Patient"]

# Mock user database
USERS = {
    "admin": {"password": "123", "role": "Admin"},
    "doctor": {"password": "123", "role": "Doctor"},
    "nurse": {"password": "123", "role": "Nurse"},
    "radiologist": {"password": "123", "role": "Radiologist"},
    "labtechnician": {"password": "123", "role": "LabTechnician"},
    "patient": {"password": "123", "role": "Patient"},
}

class UserLogin(BaseModel):
    email: str
    password: str

def create_jwt_token(email: str, role: str) -> str:
    """Create JWT token with user data."""
    payload = {
        "user_id": 1,  # Mock user ID
        "email": email,
        "role": role,
        "iat": datetime.utcnow().timestamp()  # Token creation time
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

@app.post("/login")
async def login(user: UserLogin):
    user_data = USERS.get(user.email)

    if not user_data or user_data["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_jwt_token(user.email, user_data["role"])

    return {
        "token": token,
        "token_type": "bearer",
        "email": user.email,
        "role": user_data["role"],
        "userId": 1  # Mock user ID
    }

@app.get("/protected")
async def protected_route(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]  # Remove "Bearer " prefix
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"message": "Access granted", "user_data": payload}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")