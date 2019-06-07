from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from flask import current_app
from flask_login import UserMixin
from TC_Stand import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.String(20), unique=True, nullable=False)
    
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")

    contact = db.Column(db.Integer, nullable=False)
    
    password = db.Column(db.String(60), nullable=False)

    cars = db.relationship('Vehicle', backref="owner", lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        else:
            return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    brand = db.Column(db.String(20), nullable=False)
    
    model = db.Column(db.String(20), nullable=False)
    
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    making_date = db.Column(db.Date, nullable=False)
    
    price = db.Column(db.Numeric(10,2), nullable=False)

    fuel = db.Column(db.String(20), nullable=False)
    
    capacity = db.Column(db.Integer, nullable=False)
    
    horsepower = db.Column(db.Integer, nullable=False)
    
    kilometers = db.Column(db.Integer, nullable=False)
    
    description = db.Column(db.Text, nullable=False, default="No Description Available...")

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    pics = db.relationship("Vehicle_Pic", backref="car", lazy=True)

    def __repr__(self):
        return f"Vehicle('{self.brand}', '{self.model}', '{self.making_date}')"


class Vehicle_Pic(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    image = db.Column(db.String(20), nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"), nullable=False)

    def __repr__(self):
        return f"Vehicle_Pic('{self.image}, {self.car.brand}, {self.car.model}')"
