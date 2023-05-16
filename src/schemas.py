from pydantic import BaseModel
from typing import Optional

class CreateProduct(BaseModel):
    id: Optional[int] = None
    name: str
    stock: int
    price: float | None = None
    brand: str 
    
class UpdateProduct(BaseModel):
    name: Optional[str] = None
    stock: Optional[int] = None 
    price: Optional[float] = None
    brand: Optional[str] = None
