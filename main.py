import joblib
import pandas as pd
from model import HouseDetails
from fastapi import FastAPI

model = joblib.load("house_price_model.joblib")

app = FastAPI(

    title="House prediction API",
    description="Lets check your dream house price",
    docs_url="/doc",
    redoc_url="/redoc"
)

@app.get("/")
def home():
    return {"message": "House Price Prediction API is running"}


@app.post("/predict")
def predict_price(house:HouseDetails):
    input_data=pd.DataFrame([house.model_dump()])
    prediction=model.predict(input_data)
    return{
        "predicted_price":round(float(prediction[0]),2)
    } 