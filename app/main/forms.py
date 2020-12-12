from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class PipeSizingForm(FlaskForm):
    load = StringField("Load [kW]", validators=[NumberRange(min=0.05, max=50000)])
    diameter = StringField(
        "Internal diameter [mm]", validators=[NumberRange(min=5, max=800)]
    )
    temperature = StringField(
        "Temperature [degC]", validators=[NumberRange(min=-25, max=95)]
    )
    temp_difference = StringField(
        "Temperature difference [K]", validators=[NumberRange(min=1, max=60)]
    )
    submit = SubmitField("Submit")
