from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import (StringField, FloatField, DateField, SelectField, 
                    IntegerField, TextAreaField, MultipleFileField, SubmitField)
from wtforms.validators import DataRequired, Email


class VehicleForm(FlaskForm):
    brand = StringField("Brand", validators=[DataRequired()])

    model = StringField("Model", validators=[DataRequired()])

    making_date = DateField("Month/Year", render_kw={"placeholder": "mm/yyyy"}, 
                            format="%m/%Y", validators=[DataRequired()])

    price = FloatField("Price", validators=[DataRequired()])

    fuel = SelectField("Fuel Type", validators=[DataRequired()], 
                                    choices=[("Diesel", "Diesel"), ("Gasoline", "Gasoline"), 
                                            ("Eletric", "Eletric"), ("Hybrid", "Hybrid")])

    capacity = IntegerField("Capacity", validators=[DataRequired()])

    horsepower = IntegerField("Horsepower", validators=[DataRequired()])

    kilometers = IntegerField("Kilometers", validators=[DataRequired()])

    description = TextAreaField("Description", render_kw={"style": "resize: none;", "rows": 6})

    pics = MultipleFileField("File(s) Upload", validators=[FileAllowed(["jpg", "png"])])

    submit = SubmitField("Add")




class EmailForm(FlaskForm):
    recipient = StringField("To", validators=[DataRequired(), Email()],
                                render_kw={"readonly": True})

    subject = StringField("Subject", validators=[DataRequired()])

    body = TextAreaField("Body", validators=[DataRequired()], 
                                render_kw={"style": "resize: none;", "rows": 6})

    submit = SubmitField("Send Email")