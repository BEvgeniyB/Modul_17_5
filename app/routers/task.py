from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models.user import User
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix="/task",tags=["task"])


@router.get("/")
async def get_task():
    pass

@router.get("/task_id")
async def all_tasks():
    pass

@router.post ("/create")
async def create_task():
    pass

@router.put("/update")
async def update_tas():
    pass

@router.delete("/delete")
async def delete_task():
    pass