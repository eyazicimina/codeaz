
from w11_preprocess import *

#! <preprocess>

# load from pickle
# GELEN VERIYI (SATIRI, ROW), predict yap, sonucu YAZ/GOSTER

from fastapi import FastAPI
import uvicorn
import pickle

#: Load the model
model = pickle.load(open("w11.pickle", "rb"))  # r == read, w == write, rb/wb => binary

app = FastAPI()

@app.get("/predict")
async def predict(age: int, salary: float, gender: str):
	row = {'Age': age, 'Salary': salary, 'Gender': gender}
	row = preProcessRow( row )
	row = list(row.values())
	return {"result": model.predict( [row] )[0]}

uvicorn.run(app, host="0.0.0.0", port=7000)
# http://localhost:7000/predict?age=34&salary=1000&gender=F



