from pydantic import BaseModel
from typing import Optional

class InventoryBase(BaseModel):
    name: str
    type: str
    quantity: int
    status: Optional[str] = "Verfügbar"
    description: Optional[str] = None

class InventoryCreate(InventoryBase):
    pass

class InventoryUpdate(BaseModel):
    name: Optional[str]
    type: Optional[str]
    quantity: Optional[int]
    status: Optional[str]
    description: Optional[str]

class Inventory(InventoryBase):
    id: int

    class Config:
        orm_mode = True