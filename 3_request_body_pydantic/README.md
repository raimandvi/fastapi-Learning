## Request Body & Pydantic Models

This module explains how to handle request body in FastAPI using Pydantic models.

### Topics Covered
- Request Body
- POST API
- Pydantic BaseModel
- Automatic validation

### Example JSON
{
  "name": "Amit",
  "age": 20,
  "email": "amit@gmail.com"
}

## Pydantic = data validation library
   FastAPI uses this for validate the request body.
   OR "FastAPI uses Pydantic models for data validation."
   
## Code explanation

  app = FastAPI()  ## Object of FastAPI , it controls whole API.
  class Student(BaseModel):  ## Creating pydantic model, It tells the clients about which data to be send.