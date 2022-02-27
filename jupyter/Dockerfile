FROM python:3.7.7-slim-stretch

WORKDIR /src

COPY requirements.txt /src

RUN python -m pip install pip==22.0.3 \
    && pip install -r requirements.txt \
    && mkdir /notebooks



CMD jupyter notebook --no-browser --port 7777 --allow-root --ip 0.0.0.0 --NotebookApp.token='' --NotebookApp.notebook_dir=/notebooks


# docker run -d -p 7777:7777 -v /c/py/liveproj/jupyter/notebooks:/notebooks   -v /c/py/liveproj/jupyter/data:/data  jup