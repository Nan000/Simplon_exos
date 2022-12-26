from typing import Union
from fastapi import FastAPI


import pickle
import pandas as pd


app = FastAPI()

@app.get("/")


def predict(size: Union[int,None] = "1000",
            area_type : Union[str,None] = "Super Area",
            city : Union[str,None] = "Kolkata",
            point_of_contact : Union[str,None] = "Contact Owner"):

    X_appartment = X_appartment_build(size, area_type, city, point_of_contact)
    pickled_model = pickle.load(open("pipline.pkl", "rb"))
    prediction = pickled_model.predict(X_appartment)[0]
    return {"Prediction": f"{prediction}"}

def X_appartment_build(size, area_type, city, point_of_contact):
    X_appartment = pd.DataFrame({
        "Size" : [size],
        "Area Type" : [area_type],
        "City" : [city],
        "Point of Contact" : [point_of_contact]
        })
    return X_appartment


# uvicorn fast_api:app --reload

#http://127.0.0.1:8000/?size=1000&area_type=Super%20Area&city=Kolkata&point_of_contact=Contact%20Owner
