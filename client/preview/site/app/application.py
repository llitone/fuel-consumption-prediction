import requests

from flask import Flask, render_template

from . import config
from .forms.form import PredictionForm

application = Flask(__name__)
application.config['SECRET_KEY'] = 'secret'


@application.route("/", methods=["POST", "GET"])
def index():
    form = PredictionForm()
    if form.validate_on_submit():
        data = requests.post(
            f"http://{config.API_URL}/api/v1.0/models/fuel/",
            json={
                "model": f"{config.MODEL_TYPE}_fuel_130_v1",
                "data": [
                    [
                        form.production.data, form.heat_release.data
                    ],
                ]
            }
        )
        try:
            return render_template("result.html", result=data.json()[0])
        except TypeError:
            return render_template("result.html", result=data.text)

    return render_template('prediction.html', title='123', form=form)
