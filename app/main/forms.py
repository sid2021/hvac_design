from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField, SubmitField
from wtforms.fields.core import FloatField
from wtforms.validators import NumberRange


class PipeSizingForm(FlaskForm):
    load = DecimalField("Load [kW]", validators=[NumberRange(min=0.05, max=50000)])
    pipe_type = SelectField(
        "Pipe type", choices=[("Carbon steel"), ("PPstabi"), ("PEX")]
    )
    temperature = DecimalField(
        "Temperature [degC]", validators=[NumberRange(min=-25, max=95)]
    )
    temp_difference = DecimalField(
        "Temperature difference [K]", validators=[NumberRange(min=1, max=60)]
    )
    submit = SubmitField("Submit")
