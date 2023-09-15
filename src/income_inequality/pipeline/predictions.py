

import joblib 
import numpy as np 
import pandas as pd 
from pathlib import Path 


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('final_model/income_model.pkl'))


    def predict(self, data):
        prediction = self.model.predict(data)


        return prediction