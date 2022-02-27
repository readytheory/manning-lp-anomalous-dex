FROM python:3.7.7-slim-stretch

WORKDIR /src

RUN pip install jupyter

RUN mkdir /notebooks



CMD jupyter notebook --no-browser --port 7777 --allow-root --ip 0.0.0.0 --NotebookApp.token='' --NotebookApp.notebook_dir=/notebooks