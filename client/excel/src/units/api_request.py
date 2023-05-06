import requests
from ..config import url, model


class APIRequest(object):
    def __init__(self, request_url: str = f"http://{url}/api/v1.0/models/fuel/"):
        self.url = request_url
        self.model = model
        self.data = []

    def jsonify(self):
        return dict(model=self.model, data=self.data)

    def append(self, *args):
        self.data.append(list(args))

    def __call__(self) -> int:
        request = requests.post(
            self.url, json=self.jsonify()
        )
        return request.json()

