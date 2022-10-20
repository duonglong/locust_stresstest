from locust import TaskSet, between, HttpUser, task, FastHttpUser
from hyper.contrib import HTTP20Adapter

class User(HttpUser):
    #network_timeout = 5.0
    #connection_timeout = 5.0
    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.client.mount(self.host, HTTP20Adapter())

    @task
    def index(self):
        self.client.get("/")

