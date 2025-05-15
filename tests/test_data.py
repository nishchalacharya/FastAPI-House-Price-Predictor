import pytest as pytest

from fastapi.testclient import TestClient
from fuse_nishchal.main import app


client= TestClient(app)


# def test_code_is_tested():
#     assert False
#     # return True
   
   
   
def test_predict():
    response = client.post("/predict", json={
        "Longitude": -118.25,
        "Latitude": 34.05,
        "HouseAge": 20,
        "AveBedrms": 3,
        "Population": 1000,
        "AveRooms": 5,
        "AveOccup": 2,
        "MedInc": 3
    })
    assert response.status_code == 200
    assert "prediction" in response.json()
   
    
    
  
