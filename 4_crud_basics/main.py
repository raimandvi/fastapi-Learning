from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Step 1: Pydantic model
class Student(BaseModel):
    id: int
    name: str
    age: int

# Step 2: In-memory database
students: List[Student] = []


# CREATE - Add new student
@app.post("/students")
def add_student(student: Student):
    students.append(student)
    return {"message": "Student added successfully", "student": student}


# READ - Get all students
@app.get("/students")
def get_students():
    return students


# READ - Get student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


# UPDATE - Update student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return {"message": "Student updated", "student": updated_student}
    raise HTTPException(status_code=404, detail="Student not found")


# DELETE - Delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            students.pop(index)
            return {"message": "Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found")
