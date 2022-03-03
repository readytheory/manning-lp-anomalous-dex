# curl commands

## prediction and score
curl -X 'POST' \
  'http://localhost:8000/prediction' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "vector": [
    1.2, 2.2
  ],
  "score": true
}'

## score only
curl -X 'POST' \
  'http://localhost:8000/prediction' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "vector": [
    1.2, 2.2
  ],
  "score": true
}'

## model metadata

curl -X 'GET' \
  'http://localhost:8000/model_information' \
  -H 'accept: application/json'
