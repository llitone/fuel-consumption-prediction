import requests


class APIRequest(object):
    def __init__(self, url: str):
        self.url = url
        self.model = "catboost_fuel_130_v1"
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

