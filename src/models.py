from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    stock = Column(Integer, nullable=False)
    price = Column(Float, nullable=True)
    brand = Column(String, nullable=True)
    
