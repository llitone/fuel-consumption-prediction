from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

from units.models import Models

application = Flask(__name__)

CORS(application, resource={
    r"/*": {
        "origins": "*"
    }
})
models = Models()


@application.route("/")
def index():
    return "hello world"


@application.route(f"/api/v1.0/models/fuel/", methods=["POST"])
def register_user():
    if not request.json:
        response = make_response(jsonify({"error": "keys not success"}), 400)
        return response
    if tuple(request.json.keys()) != ("model", "data"):
        response = make_response(jsonify({"error": "keys not success"}), 400)
        return response
    if not isinstance(request.json["model"], str):
        response = make_response(jsonify({"error": "model must be str"}), 400)
        return response
    if not isinstance(request.json["data"], list):
        response = make_response(jsonify({"error": "data must be list"}), 400)
        return response
    return models[request.json["model"]].predict(request.json["data"])
