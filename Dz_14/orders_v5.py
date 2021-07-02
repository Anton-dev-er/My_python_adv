from envparse import Env
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


env = Env()
DB_URL = env.str("CONN")


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)


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
    serial_no = db.Column(db.Integer, nullable=False)
    create_dt = db.Column(db.DateTime, default=datetime.utcnow())
    creator_id = db.Column(db.Integer, db.ForeignKey('employee.employee_id'), nullable=False)


if __name__ == "__main__":
    db.drop_all()
    # d = Deparments(department_name="1234")
    # db.session.add(d)
    # db.session.commit()
    #
    # e = Employee(department_id=d.department_id, position="Test")
    # db.session.add(e)
    # db.session.commit()
    #
    # o = Orders(order_type="Active", status="Tets_status", serial_no=12456, creator_id=e.employee_id)
    # db.session.add(o)
    # db.session.commit()
