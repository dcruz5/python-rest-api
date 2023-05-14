from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    stock: int
    price: float | None = None
    brand: str = None
    
class UpdateItem(BaseModel):
    name: Optional[str] = None
    stock: Optional[int] = None 
    price: Optional[float] = None
    brand: Optional[str] = None
    category: Optional[str] = None
