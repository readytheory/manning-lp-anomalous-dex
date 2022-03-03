import requests

url = "http://localhost:8000/prediction"

result = requests.post(url=url, json ={'vector':[1.3, 2.0],
                                       'score': True})

print(result)
print(result.json())

info = requests.get("http://localhost:8000/model_information")

print(info.json())
