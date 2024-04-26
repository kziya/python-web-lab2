from fastapi import FastAPI

from .db import Base, engine
from .food import food_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(food_router.router)
