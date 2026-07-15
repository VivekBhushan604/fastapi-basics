from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel,EmailStr,Field

app = FastAPI()

#Day21

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}


@app.get("/about")
def about():
    return {
        "name": "Vivek Bhushan",
        "title": "AI/ML Intern"
    }

# Day22

students = {
    1: {
        "name": "Vivek Bhushan",
        "course": "B.Tech CSE"
    },
    2: {
        "name": "KS Aravind",
        "course": "B.Tech AI"
    },
    3: {
        "name": "Ayushmaan",
        "course": "B.Tech ECE"
    }
}

@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return students[student_id]

# Day23

@app.get("/calculate")
def calculate(num1: float, num2: float, operation: str):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return {"error": "Division by zero is not allowed"}
        result = num1 / num2
    elif operation == "power":
        result = num1 ** num2
    elif operation == "modulus":
        if num2 == 0:
            return {"error": "Modulus by zero is not allowed"}
        result = num1 % num2
    else:
        return {"error": "Invalid operation"}

    return {
        "num1": num1,
        "num2": num2,
        "operation": operation,
        "result": result
    }

# Day24

class User(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=8)

@app.post("/register")
def register_user(user: User):
    return {
        "message": "User registered successfully",
        "name": user.name,
        "email": user.email
    }