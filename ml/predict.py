from pathlib import Path

import joblib
import pandas as pd


MODELS_DIR = Path(__file__).parent / "models"

model = joblib.load(MODELS_DIR / "delay_model.pkl")
preprocessor = joblib.load(MODELS_DIR / "delay_preprocessor.pkl")


def predict_delay(flight_data):
    df = pd.DataFrame([flight_data])

    processed_data = preprocessor.transform(df)

    prediction = model.predict(processed_data)[0]
    probability = model.predict_proba(processed_data)[0][1]

    if prediction == 1:
        prediction_label = "Delayed"
    else:
        prediction_label = "Not Delayed"

    return {
        "prediction": prediction_label,
        "delay_probability": round(probability, 4)
    }

