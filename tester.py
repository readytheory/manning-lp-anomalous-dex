# manning liveproject beta step 7.1 -- AnomalousDex Inc

import requests
from random import Random

r = Random()

def load_csv_with_header(filename):
    """Read a two column csv, each part is a float"""
    with open(filename) as csv:
        # discard the header by reading one line
        next(csv)
        rows = []
        for row in csv:
            mean, sd = row.split(',')
            rows.append([float(mean), float(sd)])
    return rows


datums = load_csv_with_header("./jupyter/data/test.csv")

print("Here goes nothing", flush=True)

success_count = 0
fail_count = 0

for counter, datum in enumerate(datums):
    score_flag = True if r.randint(0, 3) == 0 else False
    result = requests.post("http://localhost:7777/prediction",
                           json={'vector': datum,
                                 'score': score_flag})
    if result.status_code == 200:
        success_count += 1
    else:
        fail_count += 1
    if counter % 1000 == 0:
        print(f"{counter=}")

print("There it went", flush=True)
print(f"{success_count=} / {fail_count=}")

