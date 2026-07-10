from fastapi import FastAPI, HTTPException, status

app = FastAPI()

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

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}


@app.get("/about")
def about():
    return {
        "name": "Vivek Bhushan",
        "title": "AI/ML Intern"
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