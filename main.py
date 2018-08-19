import time
import requests

class Calculator:
    def sum(self, a, b):
#        time.sleep(10) # long running process
        return a + b

    def diff(self, a, b):
#        time.sleep(10) # long running process
        return a - b


class Blog:
    def __init__(self, name):
        self.name = name

    def posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")

        return response.json()

    def __repr__(self):
        return '<Blog: {}>'.format(self.name)