from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os
import numpy as np  

# Initialize FastAPI
app = FastAPI()

# Load the trained model
model_path = os.path.join("models", "gradient_boosting.joblib")
model = joblib.load(model_path)

# Define input data structure (list of lists)
class InputData(BaseModel):
    features: list[list[float]]

# Define prediction endpoint
@app.post("/predict/")
def predict(data: InputData):
    try:
        # Convert input data into a DataFrame
        input_df = pd.DataFrame(data.features)

        # Make predictions
        predictions = model.predict(input_df).tolist()
        probabilities = model.predict_proba(input_df)[:, 1].tolist()
        
        # Return results
        return {"predictions": predictions, "probabilities": probabilities}
    except Exception as e:
        return {"error": str(e)}
