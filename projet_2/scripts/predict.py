import joblib
import pandas as pd
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = joblib.load('model.joblib')

# définir le modèle d'entrée
class InputFeatures(BaseModel):
    age: int
    bmi: float
    children: int
    sexe: str
    smoker: str
    region: str
    
@app.post("/predict")
def predict(input: InputFeatures):
    features= np.array([[input.age, input.bmi, input.children, input.sexe, input.smoker, input.region]])
    features = pd.DataFrame(features, columns=["age", "bmi", "children", "sexe", "smoker", "region"])
    prediction = model.predict(features)
    return {"prediction": float(prediction[0])}
