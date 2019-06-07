from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField

class FilterForm(FlaskForm):
    brand = StringField("Brand")

    model = StringField("Model")

    fuel = SelectField("Fuel", choices=[("Diesel", "Diesel"), ("Gasoline", "Gasoline"), 
                                        ("Eletric", "Eletric"), ("Hybrid", "Hybrid")])

    submit = SubmitField("Search")