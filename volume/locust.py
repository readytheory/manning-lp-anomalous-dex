from locust import HttpUser, task, between, User
from random import Random


r = Random()


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    

    @task(2)
    def hello_world(self):
        self.client.get("/model_information")

    @task(3)
    def do_some_stuff(self):
        v = [1.2, 5]
        tf = True if r.randint(0, 1) == 0 else False
        mean = r.random()
        sd = r.random()
        for item_id in range(10):
            self.client.post("/prediction",
                             json={'vector': v, 'score': tf})


if __name__ == '__main__':
    qs = QuickstartUser(environment='pest')
    qs.do_some_stuff()

