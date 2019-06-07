from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import (StringField, SubmitField, PasswordField, 
                    FileField, IntegerField, BooleanField)
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from flask_login import current_user
from TC_Stand.models import User


class RegistrationForm(FlaskForm):
    username = StringField("Username", 
                            validators=[DataRequired(), Length(min=4, max=20)])
    
    email = StringField("Email", 
                            validators=[DataRequired(), Email()])

    contact = IntegerField("Contact", validators=[DataRequired()])

    password = PasswordField("Password", 
                            validators=[DataRequired()])
    
    confirm_password = PasswordField("Confirm Password", 
                            validators=[DataRequired(), EqualTo("password")])

    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError("That username is taken. Please choose a different one.")

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()

        if email:
            raise ValidationError("That email is taken. Please choose a different one.")

    def validate_contact(self, contact):
        try:
            int(contact.data)
        except:
            raise ValidationError("Please insert a valid contact number.")


class LoginForm(FlaskForm):
    email = StringField("Email", 
                            validators=[DataRequired(), Email()])

    password = PasswordField("Password", 
                            validators=[DataRequired()])

    remember = BooleanField("Remember Me")
    
    submit = SubmitField("Log In")


class UpdateAccountForm(FlaskForm):
    username = StringField("Username", 
                            validators=[DataRequired(), Length(min=4, max=20)])
    
    email = StringField("Email", 
                            validators=[DataRequired(), Email()])

    contact = IntegerField("Contact", validators=[DataRequired()])

    picture = FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "png"])])

    submit = SubmitField("Update")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()

            if user:
                raise ValidationError("That username is taken. Please choose a different one.")

    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()

            if email:
                raise ValidationError("That email is taken. Please choose a different one.")

    def validate_contact(self, contact):
        try:
            int(contact.data)
        except:
            raise ValidationError("Please insert a valid contact number.")


class RequestResetForm(FlaskForm):
    email = StringField("Email",
                                validators=[DataRequired(), Email()])

    submit = SubmitField("Request Password Reset")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if not user:
            raise ValidationError("There is no account with that email. You must register first.")


class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", 
                        validators=[DataRequired()])
    
    confirm_password = PasswordField("Confirm Password", 
                        validators=[DataRequired(), EqualTo("password")])

    submit = SubmitField("Reset Password")