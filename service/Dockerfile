FROM python:3.7.7-slim-stretch

WORKDIR /src

COPY model.joblib requirements.txt /src

RUN python -m pip install pip==22.0.3 \
    && pip install -r requirements.txt

COPY main.py /src

CMD uvicorn --port 7777 --host 0.0.0.0 main:app


# docker run -d -p 7777:7777 levin/lp-service