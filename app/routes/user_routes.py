from fastapi import APIRouter, HTTPException,status
from schemas.user import User, UserCreate, UserUpdate
from typing import List
from datetime import datetime
from db.user_db import users_db



user_router = APIRouter()



@user_router.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    user_id = len(users_db) + 1
    new_user = User(id=user_id, **user.model_dump())  
    users_db.append(new_user)
    return new_user


@user_router.get("/users/", response_model=List[User], status_code=status.HTTP_200_OK)
def get_users():
    return users_db


@user_router.get("/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def get_user(user_id: int):
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@user_router.put("/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user_update: UserUpdate):
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    user_data = user.model_dump()  
    user_data.pop("id", None)  
    
    updated_data = user_update.model_dump(exclude_unset=True)
    user_data.update(updated_data) 

    updated_user = User(id=user.id, **user_data)
    users_db[users_db.index(user)] = updated_user
    return updated_user


@user_router.patch("/users/{user_id}", status_code=status.HTTP_200_OK)
def deactivate_user(user_id: int):
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user.is_active = False
    return {"message": "User deactivated successfully"}


@user_router.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int):
    user = next ((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    users_db.remove(user)
    return {"message": "User deleted successfully"}

