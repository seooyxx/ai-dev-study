# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from model.model import SentimentModel

app = FastAPI()
model = SentimentModel()

class TextInput(BaseModel):
    text: str

# 예측할 때 /predict로 많이 씀
@app.post("/predict")
async def predict_sentiment(input: TextInput):
    prediction = model.predict(input.text)
    return {"text": input.text, "sentiment": prediction}
