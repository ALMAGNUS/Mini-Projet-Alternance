from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.region_model import Region
from modules.database import get_db

router = APIRouter()

@router.post("/")
def create_region(region_name: str, db: Session = Depends(get_db)):
    new_region = Region(region_name=region_name)
    db.add(new_region)
    db.commit()
    db.refresh(new_region)
    return new_region

@router.get("/")
def read_regions(db: Session = Depends(get_db)):
    regions = db.query(Region).all()
    return regions

@router.get("/{region_id}")
def read_region(region_id: int, db: Session = Depends(get_db)):
    region = db.query(Region).filter(Region.id_region == region_id).first()
    if region is None:
        raise HTTPException(status_code=404, detail="Region not found")
    return region

@router.put("/{region_id}")
def update_region(region_id: int, region_name: str, db: Session = Depends(get_db)):
    region = db.query(Region).filter(Region.id_region == region_id).first()
    if region is None:
        raise HTTPException(status_code=404, detail="Region not found")
    region.region_name = region_name
    db.commit()
    db.refresh(region)
    return region

@router.delete("/{region_id}")
def delete_region(region_id: int, db: Session = Depends(get_db)):
    region = db.query(Region).filter(Region.id_region == region_id).first()
    if region is None:
        raise HTTPException(status_code=404, detail="Region not found")
    db.delete(region)
    db.commit()
    return {"message": "Region deleted successfully"}
