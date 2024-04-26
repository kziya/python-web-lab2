from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)

    orders = relationship("Order", back_populates="user")