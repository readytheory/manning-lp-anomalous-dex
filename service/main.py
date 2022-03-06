from json import dumps
from typing import Optional, List
from prometheus_client import make_asgi_app, Counter as PromCounter, Histogram

from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load

clf = load("model.joblib")

app = FastAPI()

metrics_asgi_app = make_asgi_app()

app.mount(path="/metrics", app=metrics_asgi_app)

prediction_counter = PromCounter(name="prediction_counter", documentation="Count of POST calls to prediction")
model_info_counter = PromCounter(name="model_info_counter", documentation="Count of GET calls to model info")
with_score_histogram = Histogram(name='prediction_with_score_histogram',documentation='Calls to prediction')
no_score_historgram = Histogram(name='prediction_no_score_histogram',documentation='Calls to prediction without score')
latency_histogram = Histogram(name='latency_histogram',documentation='latency to prediction')



class FeatureVector(BaseModel):
    vector: List[float]
    score: Optional[bool] = None


@app.post("/prediction")
def prediction(vec: FeatureVector):
    prediction_counter.inc()

    with latency_histogram.time():
        retval = clf.predict([vec.vector])
    retval = int(retval)
    response = {'is_inlier': retval}
    if vec.score:
        score = clf.score_samples([vec.vector])
        score = float(score)
        response['anamoly_score'] = score
        with_score_histogram.observe(score)
    else:
        no_score_historgram.observe(retval)
    return response

@app.get("/model_information")
def model_information():
    model_info_counter.inc()
    return clf.get_params()





