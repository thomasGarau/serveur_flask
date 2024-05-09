import joblib
import pandas as pd
import os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'modele', 'model.pkl')
model = joblib.load(model_path)
model = joblib.load('modele/model.pkl')


def predict(data):
    print(data)
    return True
    # df = pd.DataFrame([data])
    # prediction = model.predict(df)
    # return {"prediction": prediction.tolist()}