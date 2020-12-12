from app.main import bp
from flask import render_template
from app.main.forms import PipeSizingForm


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/water", methods=["GET", "POST"])
def water():
    form = PipeSizingForm()
    if form.validate_on_submit():
        pass
    return render_template("water.html", form=form)
