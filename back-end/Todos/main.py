from fastapi import FastAPI
from models import Todos
from database import engine,SessionLocal
from routers import auth,todos,admin,users
import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(admin.router)
app.include_router(todos.router)
