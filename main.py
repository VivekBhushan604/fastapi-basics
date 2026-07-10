from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}


@app.get("/about")
def about():
    return {
        "name": "Vivek Bhushan",
        "title": "AI/ML Intern"
    }
