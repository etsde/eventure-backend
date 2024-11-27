from sqlalchemy.orm import Session
from models import Inventory
from schemas import InventoryCreate, InventoryUpdate

def get_inventory(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Inventory).offset(skip).limit(limit).all()

def create_inventory(db: Session, inventory: InventoryCreate):
    db_item = Inventory(**inventory.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_inventory(db: Session, inventory_id: int, updates: InventoryUpdate):
    db_item = db.query(Inventory).filter(Inventory.id == inventory_id).first()
    if db_item:
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_inventory(db: Session, inventory_id: int):
    db_item = db.query(Inventory).filter(Inventory.id == inventory_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
