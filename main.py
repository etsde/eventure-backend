from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
from crud import get_inventory, create_inventory, update_inventory, delete_inventory
from schemas import InventoryCreate, InventoryUpdate, Inventory

# Datenbanktabellen erstellen
Base.metadata.create_all(bind=engine)

# FastAPI-App initialisieren
app = FastAPI()

# Dependency für die Datenbank-Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/inventory", response_model=list[schemas.Inventory])
def read_inventory(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_inventory(db, skip=skip, limit=limit)

@app.post("/inventory", response_model=schemas.Inventory)
def create_inventory(inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    return crud.create_inventory(db, inventory)

@app.patch("/inventory/{inventory_id}", response_model=schemas.Inventory)
def update_inventory(inventory_id: int, updates: schemas.InventoryUpdate, db: Session = Depends(get_db)):
    item = crud.update_inventory(db, inventory_id, updates)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/inventory/{inventory_id}")
def delete_inventory(inventory_id: int, db: Session = Depends(get_db)):
    item = crud.delete_inventory(db, inventory_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
