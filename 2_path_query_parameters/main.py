from fastapi import FastAPI

app = FastAPI()

# --------------------
# Path Parameter
# --------------------
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id,
        "message": "Student fetched successfully"
    }


# --------------------
# Query Parameter
# --------------------
@app.get("/students")
def get_students(skip: int = 0, limit: int = 10):
    return {
        "skip": skip,
        "limit": limit,
        "message": "Students list"
    }
