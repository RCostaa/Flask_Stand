from flask import (render_template, url_for, flash, redirect, 
                    request, abort, Blueprint)
from flask_login import current_user, login_required
from TC_Stand import db
from TC_Stand.models import Vehicle, Vehicle_Pic
from TC_Stand.vehicles.forms import VehicleForm, EmailForm
from TC_Stand.vehicles.utils import send_email, save_vehicle_picture

vehicles = Blueprint("vehicles", __name__)


@vehicles.route("/vehicle/new", methods=["GET", "POST"])
@login_required
def new_vehicle():
    form = VehicleForm()
    if form.validate_on_submit():              
        if form.description.data:          
            vehicle = Vehicle(brand=form.brand.data,
                                model=form.model.data,
                                making_date=form.making_date.data,
                                price=form.price.data,
                                fuel=form.fuel.data,
                                capacity=form.capacity.data,
                                horsepower=form.horsepower.data,
                                kilometers=form.kilometers.data,
                                description=form.description.data,
                                owner=current_user)
        else:
            vehicle = Vehicle(brand=form.brand.data,
                                model=form.model.data,
                                making_date=form.making_date.data,
                                price=form.price.data,
                                fuel=form.fuel.data,
                                capacity=form.capacity.data,
                                horsepower=form.horsepower.data,
                                kilometers=form.kilometers.data,
                                owner=current_user)
        
        if form.pics.data:
                pics = request.files.getlist(form.pics.name)
                
                if pics:
                    for pic in pics:
                        if pic.filename != "":
                            filename = save_vehicle_picture(pic, (500, 300))
                                
                            image = Vehicle_Pic(image=filename, car=vehicle)
                            db.session.add(image)
        
        db.session.add(vehicle)
        db.session.commit()
        flash("Your vehicle has been added!", "success")
        return redirect(url_for("main.home"))

    return render_template("create_vehicle.html", title="New Vehicle", form=form, legend="Add")


@vehicles.route("/vehicle/<int:vehicle_id>", methods=["GET", "POST"])
def vehicle(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    form = EmailForm()
    if form.validate_on_submit():
        send_email(form)
        flash(f"An email has been sent to the user {vehicle.owner.username}", "info")
    elif request.method == "GET":
        form.recipient.data = vehicle.owner.email

    return render_template("vehicle.html", title=vehicle.brand+vehicle.model, vehicle=vehicle, form=form)


@vehicles.route("/vehicle/<int:vehicle_id>/update", methods=["GET", "POST"])
@login_required
def update_vehicle(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    if vehicle.owner != current_user:
        abort(403)

    form = VehicleForm()
    if form.validate_on_submit():
        vehicle.brand = form.brand.data
        vehicle.model = form.model.data
        vehicle.making_date = form.making_date.data
        vehicle.price = form.price.data
        vehicle.fuel = form.fuel.data
        vehicle.capacity = form.capacity.data
        vehicle.horsepower = form.horsepower.data
        vehicle.kilometers = form.kilometers.data
        if form.description.data:
            vehicle.description = form.description.data

        db.session.commit()
        flash("Your vehicle has been updated!", "success")
        return redirect(url_for("vehicles.vehicle", vehicle_id=vehicle.id))
        
    elif request.method == "GET":
        form.brand.data = vehicle.brand
        form.model.data = vehicle.model
        form.making_date.data = vehicle.making_date
        form.price.data = int(vehicle.price)
        form.fuel.data = vehicle.fuel
        form.capacity.data = vehicle.capacity
        form.horsepower.data = vehicle.horsepower
        form.kilometers.data = vehicle.horsepower
        form.description.data = vehicle.description
    
    
    return render_template("update_vehicle.html", title= "Update Vehicle", form=form, legend="Update")


@vehicles.route("/vehicle/<int:vehicle_id>/delete", methods=["POST"])
@login_required
def delete_vehicle(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)

    if vehicle.owner != current_user:
        abort(403)
    
    if vehicle.pics:
        for pic in vehicle.pics:
            db.session.delete(pic)

    db.session.delete(vehicle)
    db.session.commit()
    flash("Your vehicle has been deleted!", "success")
    
    return redirect(url_for("main.home"))
