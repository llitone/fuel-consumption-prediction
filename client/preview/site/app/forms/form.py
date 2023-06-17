from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired


class PredictionForm(FlaskForm):
    production = FloatField('Выработка электроэнергии ТА гр.130', validators=[DataRequired()])
    heat_release = FloatField('Отпуск тепла из ТО ТА гр.130', validators=[DataRequired()])
    submit = SubmitField('Предсказать')
