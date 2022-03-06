from random import Random
from locust import HttpUser, task, between, User

r = Random()

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/model_information")

    @task(3)
    def do_some_stuff(self):
        tf = True if r.randint(0, 1) == 0 else False
        mean = r.random()
        sd = r.random()
        v = [mean, sd]
        for item_id in range(10):
            self.client.post("/prediction",
                             json={'vector': v, 'score': tf})


if __name__ == '__main__':
    qs = QuickstartUser(environment='pest')
    qs.do_some_stuff()

