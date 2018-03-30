from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class EngineDetails(FlaskForm):
    id = IntegerField('Engine ID', validators=[DataRequired()])
    desc = StringField('Description', validators=[DataRequired()])
    thrust = IntegerField('Thrust', validators=[DataRequired()])
