from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib






model=joblib.load('models/california_housing_model.pkl')
    
    
    
app = FastAPI()


class HousingData(BaseModel):
    Longitude: float
    Latitude: float
    HouseAge: float
    AveBedrms:float
    Population: float
    AveRooms: float
    AveOccup: float
    MedInc: float
 
    
        
@app.post("/predict")
def predict(data:HousingData):
    data = data.dict()
    Longitude = data['Longitude']
    Latitude = data['Latitude']
    HouseAge = data['HouseAge']
    AveBedrms = data['AveBedrms']
    Population = data['Population']
    AveRooms = data['AveRooms']
    AveOccup = data['AveOccup']
    MedInc = data['MedInc']
    
    input_data = np.array([[MedInc,HouseAge, AveRooms, AveBedrms, Population, AveOccup,Latitude,Longitude]])
    
    prediction = model.predict(input_data)
    
    return {"prediction": prediction[0]}


        