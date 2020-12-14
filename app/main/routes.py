from app.main import bp
from flask import render_template
from app.main.forms import PipeSizingForm
from app.main.controllers.water_handler import get_pipes


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/water", methods=["GET", "POST"])
def water():
    form = PipeSizingForm()
    if form.validate_on_submit():
        load = float(form.load.data)
        temperature = float(form.temperature.data)
        temp_difference = float(form.temp_difference.data)
        fluid = "water"
        pipe_type = form.pipe_type.data
        pressure_losses = get_pipes(
            load, fluid, pipe_type, temperature, temp_difference
        )
        return render_template("water.html", form=form, pressure_losses=pressure_losses)
    return render_template("water.html", form=form)
