FROM python:3.7.7-slim-stretch

WORKDIR /src

COPY main.py model.joblib requirements.txt /src

RUN python -m pip install pip==22.0.3 \
    && pip install -r requirements.txt






CMD uvicorn --port 8000 --host 0.0.0.0 main:app


# docker run -d -p 8000:8000 levin/lp-service