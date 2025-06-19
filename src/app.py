from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()
model = pickle.load(open("model.pkl", "rb"))

@app.get("/")
def root():
    return {"message": "Model running"}

@app.post("/predict")
def predict(data):
    prediction = model.predict(np.array(data).reshape(1, -1))
    return {"prediction": prediction.tolist()}