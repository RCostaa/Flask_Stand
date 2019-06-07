from flask import render_template, request, Blueprint
from TC_Stand import db
from TC_Stand.models import Vehicle
from TC_Stand.main.forms import FilterForm

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
@main.route("/home", methods=["GET", "POST"])
def home():
    page = request.args.get('page', 1, type=int)
    
    form = FilterForm()
    if form.validate_on_submit():
        filters = {}
        if form.brand.data:
            filters["brand"] = form.brand.data
        if form.model.data:
            filters["model"] = form.model.data
        filters["fuel"] = form.fuel.data

        vehicles = db.session.query(Vehicle)
        for attr, value in filters.items():
            vehicles = vehicles.filter(getattr(Vehicle, attr).like("%%%s%%" % value))

        vehicles = vehicles.order_by(Vehicle.date_posted.desc()).paginate(page=page, per_page=5)
    elif request.method == "GET":
        vehicles = Vehicle.query.order_by(Vehicle.date_posted.desc()).paginate(page=page, per_page=5)



    return render_template("home.html", vehicles=vehicles, form=form)
