from fastapi import FastAPI
from routes import (
    patient_route,
    region_route,
    sex_route,
    smoker_route
)
from sqlalchemy.orm import DeclarativeMeta
from modules.database import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(patient_route.router, prefix="/patient", tags=["patient"])
# app.include_router(appuser_route.router, prefix="/appuser", tags=["appuser"])
app.include_router(region_route.router, prefix="/region", tags=["region"])
app.include_router(sex_route.router, prefix="/sex", tags=["sex"])
app.include_router(smoker_route.router, prefix="/smoker", tags=["smoker"])