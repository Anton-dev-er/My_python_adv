from envparse import Env
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

env = Env()
DB_URL = env.str("DB_URL")

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)


class CustomersFromTg(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    chat_id = db.Column(db.Integer, nullable=False)
    is_subscribed = db.Column(db.Boolean, default=False)
    create_dt = db.Column(db.DateTime, default=datetime.utcnow())


class CustomersFromWebsite(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    create_dt = db.Column(db.DateTime, default=datetime.utcnow())


class Customers(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname_user_from_website = db.Column(db.String, db.ForeignKey('CustomersFromWebsite.nickname'), unique=True)
    nickname_user_from_telegram = db.Column(db.String, db.ForeignKey('CustomersFromTg.nickname'), unique=True)


class Deparments(db.Model):
    department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department_name = db.Column(db.String(50), unique=True)
    create_dt = db.Column(db.DateTime, default=datetime.utcnow())


class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fio = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    create_dt = db.Column(db.DateTime, default=datetime.utcnow())
    department_id = db.Column(db.Integer, db.ForeignKey('deparments.department_id'), nullable=False)


class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_type = db.Column(db.String(100), nullable=False)
    descriptions = db.Column(db.String(500))
    status = db.Column(db.String(100), nullable=False)
    create_dt = db.Column(db.DateTime, default=datetime.utcnow())
    creator_id = db.Column(db.Integer, db.ForeignKey('employee.employee_id'), nullable=False)
    customer = db.Column(db.String, db.ForeignKey('Customers.user_id'), nullable=False, unique=True)


if __name__ == "__main__":
    db.create_all()
