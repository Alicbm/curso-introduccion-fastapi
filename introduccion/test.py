from typing import Optional, List

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=2, max_length=50)
    age: Optional[int] = None
    email: str = Field(min_length=6, max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "id": 0,
                "name": 'Alic',
                "age": 0,
                "email": 'email@mail.com'
            }
        }

users = [
    {
        "id": 1,
        "name": 'Alic Barandica',
        "age": 19,
        "email": 'alic@mail.com'
    },
    {
        "id": 2,
        "name": 'pepe',
        "age": 22,
        "email": 'pepe@mail.com'
    }
]

#Get all
@app.get('/users', tags=['users'], response_model=List[User], status_code=200)
def get_users() -> List[User]:
    return users

#Find one
@app.get('/users/{id}', tags=['users'], response_model=User, status_code=200)
def find_one(id: int) -> User:
    for item in users:
        if item["id"] == id:
            return item
    return JSONResponse(status_code=404, content={ "msessage": 'User not found' })

#find by name
@app.get('/users/', tags=['users'], status_code=200, response_model=User)
def find_by_name(name: str):
    for item in users:
        if item['name'] == name:
            return item
    return JSONResponse(status_code=404, content={ "msessage": 'User not found' })

#Create
@app.post('/users', tags=['users'], response_model=User, status_code=201)
def create_one(user: User) -> User:
    users.append(user)
    return user


#update one
@app.put('/users/{id}', tags=['users'], status_code=200, response_model=User)
def update_one(id: int, user: User):
    for item in users:
        if item["id"] == id:
            item.update(user)
            return item
    return JSONResponse(status_code=404, content={ "msessage": 'User not found' })

#delete one
@app.delete('/users/{id}', tags=['users'], status_code=200, response_model=User)
def delete_one(id: int):
    for item in users:
        if item["id"] == id:
            users.remove(item)
            return item
    return JSONResponse(status_code=404, content={ "msessage": 'User not found' })








