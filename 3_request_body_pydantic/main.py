from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Step 1: Create a Pydantic model
class Student(BaseModel):
    name: str
    age: int
    email: str


# Step 2: Create POST API
@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student created successfully",
        "student_data": student
    }
