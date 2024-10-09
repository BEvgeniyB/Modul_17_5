from sqlalchemy.schema import CreateTable
from app.models import *
from app.backend.db import Base
from sqlalchemy import Column, Integer, String, BOOLEAN, ForeignKey
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {"keep_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    completed = Column(BOOLEAN, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    slug = Column(String, unique=True, index=True)

    user = relationship(argument="User", back_populates="task")


#print(CreateTable(Task.__table__))
