from typing import Type

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.food.food_model import Food


def get_food_by_name(db: Session, name: str) -> Food:
    return db.query(Food).filter(Food.name == name).first()


def created_food(db: Session, name: str, price: float) -> Food:
    isExistsFood = get_food_by_name(db, name)

    if isExistsFood:
        raise HTTPException(status_code=400, detail="Food already exists")

    food = Food(name=name, price=price)
    db.add(food)
    db.commit()
    db.refresh(food)
    return food


def get_food_by_id(db: Session, food_id: int) -> Type[Food]:
    db_food = db.query(Food).filter(food_id == Food.id).first()

    if db_food is None:
        raise HTTPException(status_code=404)

    return db_food


def updated_food(db: Session, id: int, name: str, price: float) -> Type[Food]:
    db_food = db.query(Food).filter(id == Food.id).first()
    if db_food is None:
        raise HTTPException(status_code=404)

    if name:
        isExistsFood = get_food_by_name(db, name)
        if isExistsFood:
            raise HTTPException(status_code=400, detail="Food already exists")
        setattr(db_food, 'name', name)

    if price:
        setattr(db_food, 'price', price)

    db.commit()
    db.refresh(db_food)
    return db_food


def delete_food(db: Session, food_id: int) -> None:
    db_food = db.query(Food).filter(food_id == Food.id).first()
    if db_food is None:
        raise HTTPException(status_code=404)

    db.delete(db_food)
    db.commit()
    return None
