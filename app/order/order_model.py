from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    idUser = Column(Integer, ForeignKey('users.id'))
    idFood = Column(Integer, ForeignKey('foods.id'))

    user = relationship("User", back_populates="orders")
    food = relationship("Food", back_populates="orders")