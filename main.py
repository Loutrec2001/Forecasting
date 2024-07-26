from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load('trained_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoders = joblib.load('label_encoders.pkl')
class_encoder = joblib.load('class_encoder.pkl')

# Mapeos 
class_mapping = {0: 'Alpha', 1: 'Betha'}

class PredictionInput(BaseModel):
    Partner: str
    Dependents: str
    Service1: str
    Service2: str
    Security: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    Charges: float

@app.post("/predict/")
async def predict(input_data: PredictionInput):
    try:
        
        data = pd.DataFrame([input_data.dict()])

         
        for column, le in label_encoders.items():
            if column in data.columns:
                data[column] = le.transform(data[column])
            else:
                raise HTTPException(status_code=400, detail=f"Missing column: {column}")

         
        if 'Charges' in data.columns:
            data[['Charges']] = scaler.transform(data[['Charges']])
        else:
            raise HTTPException(status_code=400, detail="Missing 'Charges' column in input data")

        
        prediction = model.predict(data)
        
         
        result = class_mapping.get(prediction[0], 'Unknown')
        
        return {"prediction": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

 
