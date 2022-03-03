from json import dumps
from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load

clf = load("model.joblib")

app = FastAPI()

class FeatureVector(BaseModel):
    vector: List[float]
    score: Optional[bool] = None

@app.post("/prediction")
def prediction(vec: FeatureVector):
    retval = clf.predict([vec.vector])
    retval = int(retval)
    response = {'is_inlier': retval}
    if vec.score:
        score = clf.score_samples([vec.vector])
        score = float(score)
        response['anamoly_score'] = score
    return response

@app.get("/model_information")
def model_information():
    return clf.get_params()





