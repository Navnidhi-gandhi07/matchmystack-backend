from fastapi import FastAPI
from .routers import auth, resume, recommend
from .db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MatchMyStack API")

app.include_router(auth.router)
app.include_router(resume.router)
app.include_router(recommend.router)

@app.get("/")
def root():
    return {"message": "Welcome to MatchMyStack Backend!"}
