from sqlalchemy import Column, Integer, String, Text, ARRAY, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String)
    bio = Column(Text)
    role = Column(String)
    resume_text = Column(Text)
    resume_embedding = Column(Vector(768))
    created_at = Column(TIMESTAMP)

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    tech_stack = Column(ARRAY(String))
    project_embedding = Column(Vector(768))

