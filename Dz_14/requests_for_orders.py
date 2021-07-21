import json

import sqlalchemy.exc
from envparse import Env
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


env = Env()
DB_URL = env.str("DB_URL")


my_app = Flask(__name__)
my_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
my_app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(my_app)


class Departments(db.Model):
    department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department_name = db.Column(db.String(50), unique=True)
    create_dt = db.Column(db.DateTime, default=datetime.utcnow())


class Employees(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fio = db.Column(db.String(100), nullable=False, unique=True)
    position = db.Column(db.String(100), nullable=False)
    create_dt = db.Column(db.DateTime, default=datetime.utcnow())
    department_id = db.Column(db.Integer, db.ForeignKey('departments.department_id'), nullable=False)


class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_type = db.Column(db.String(100), nullable=False)
    descriptions = db.Column(db.String(500))
    status = db.Column(db.String(100), nullable=False)
    serial_no = db.Column(db.Integer, nullable=False, unique=True)
    create_dt = db.Column(db.DateTime, default=datetime.utcnow())
    creator_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'), nullable=False)


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError as e:
        return True
    return False


def dep_get_dict(d):
    return {"Name": d.department_name, "Id": d.department_id, "Create date": str(d.create_dt)}


def emp_get_dict(e):
    return {"ID": e.employee_id,
            "Fio": e.fio,
            "Position": e.position,
            "Create date": str(e.create_dt),
            "Department ID": e.department_id
                }


def ord_get_dict(o):
    return {"ID": o.order_id,
            "Order type": o.order_type,
            "Descriptions": o.descriptions,
            "Status": o.status,
            "Serial_no": o.serial_no,
            "Create date": str(o.create_dt),
            "Creator ID": o.creator_id
                }


def for_create_new_param(cls):
    try:
        if issubclass(Departments, cls):
            param_list = ["department_name"]
        elif issubclass(Employees, cls):
            param_list = ["fio", "position", "department_id"]
        elif issubclass(Orders, cls):
            param_list = ["order_type", "descriptions", "status", "serial_no", "creator_id"]
        else:
            return "Wrong class"

        if request.data == b'':
            raise ValueError

        data = json.loads(request.data)

        if sorted(data.keys()) != sorted(param_list):
            raise ValueError

        if is_json(request.data):
            raise ValueError

        if issubclass(Departments, cls):
            class_instance = Departments(department_name=data["department_name"])
        elif issubclass(Employees, cls):
            d = Departments.query.get(data["department_id"])
            class_instance = Employees(fio=data["fio"],
                                       position=data["position"],
                                       department_id=d.department_id)
        elif issubclass(Orders, cls):
            e = Employees.query.get(data["creator_id"])
            class_instance = Orders(order_type=data["order_type"],
                       descriptions=data["descriptions"],
                       status=data["status"],
                       serial_no=data["serial_no"],
                       creator_id=e.creator_id)

        db.session.add(class_instance)
        db.session.commit()

    except sqlalchemy.exc.IntegrityError:
        return "Already exist"
    except ValueError:
        return f"Should be a format dict or json (with keys like:{param_list})"

    return "Successfully created"


def check_id(id_, cls):
    if issubclass(Departments, cls):
        list_id = [i.department_id for i in Departments.query.all()]
    elif issubclass(Employees, cls):
        list_id = [i.employee_id for i in Employees.query.all()]
    elif issubclass(Orders, cls):
        list_id = [i.order_id for i in Orders.query.all()]
    else:
        return True

    if id_ not in list_id:
        return True

    return False


@my_app.route("/departments/create", methods=["POST"])
def dep_create_new_param():
    return for_create_new_param(Departments)


@my_app.route("/employees/create", methods=["POST"])
def emp_create_new_param():
    return for_create_new_param(Employees)


@my_app.route("/orders/create", methods=["POST"])
def ord_create_new_param():
    return for_create_new_param(Orders)


@my_app.route("/departments/get/all", methods=["GET"])
def dep_get_data():
    return render_template('get_data.html', lst=[dep_get_dict(i) for i in Departments.query.all()])


@my_app.route("/employees/get/all", methods=["GET"])
def emp_get_data():
    return render_template('get_data.html', lst=[emp_get_dict(i) for i in Employees.query.all()])


@my_app.route("/orders/get/all", methods=["GET"])
def ord_get_data():
    return render_template('get_data.html', lst=[ord_get_dict(i) for i in Orders.query.all()])


@my_app.route("/departments/get/<int:id_>", methods=["GET"])
def dep_get_data_by_id(id_):
    if check_id(id_, Departments):
        return "Non-existent id or class"
    return dep_get_dict(Departments.query.get(id_))


@my_app.route("/employees/get/<int:id_>", methods=["GET"])
def emp_get_data_by_id(id_):
    if check_id(id_, Employees):
        return "Non-existent id or class"
    return emp_get_dict(Employees.query.get(id_))


@my_app.route("/orders/get/<int:id_>", methods=["GET"])
def ord_get_data_by_id(id_):
    if check_id(id_, Orders):
        return "Non-existent id or class"
    return dep_get_dict(Orders.query.get(id_))


def for_delete_data_by_id(id_, list_id, cls):
    try:
        if id_ not in list_id:
            return "Wrong param"
        db.session.delete(cls.query.get(id_))
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return "Key (department_id)=(1) is still referenced from table 'employees'"
    return "Successfully deleted"


@my_app.route("/departments/delete/<int:id_>", methods=["DELETE"])
def dep_delete_data_by_id(id_):
    list_id = [i.department_id for i in Departments.query.all()]
    return for_delete_data_by_id(id_=id_, list_id=list_id, cls=Departments)


@my_app.route("/employees/delete/<int:id_>", methods=["DELETE"])
def emp_delete_data_by_id(id_):
    list_id = [i.employee_id for i in Employees.query.all()]
    return for_delete_data_by_id(id_=id_, list_id=list_id, cls=Employees)


@my_app.route("/orders/delete/<int:id_>", methods=["DELETE"])
def ord_delete_data_by_id(id_):
    list_id = [i.order_id for i in Orders.query.all()]
    return for_delete_data_by_id(id_=id_, list_id=list_id, cls=Orders)


@my_app.route("/departments/update/<string:column>", methods=["POST"])
def dep_update_data_by_id(column):
    data = json.loads(request.data)

    if sorted(data.keys()) != sorted(["Id", "New_value"]):
        return f'Should be a format dict or json (with keys like:{["Id", "New_value"]})'

    if check_id(data["Id"], Departments):
        return "Non-existent id or class"

    if column == "department_name":
        d = Departments.query.get(data["Id"])
        d.department_name = data["New_value"]
        db.session.add(d)
        db.session.commit()
        return "Successfully updated"
    else:
        return "Wrong column"


@my_app.route("/employees/update/<string:column>", methods=["POST"])
def emp_update_data_by_id(column):
    data = json.loads(request.data)

    if sorted(data.keys()) != sorted(["Id", "New_value"]):
        return f'Should be a format dict or json (with keys like:{["Id", "New_value"]})'

    if check_id(data["Id"], Employees):
        return "Non-existent id or class"

    e = Employees.query.get(data["Id"])

    column_list = {
        "fio": e.fio,
        "position": e.position,
    }

    if column in column_list.keys():
        column_list[column] = data["New_value"]
    else:
        return "Wrong column"
    return "Successfully updated"


@my_app.route("/orders/update/<string:column>", methods=["POST"])
def ord_update_data_by_id(column):
    data = json.loads(request.data)

    if sorted(data.keys()) != sorted(["Id", "New_value"]):
        return f'Should be a format dict or json (with keys like:{["Id", "New_value"]})'

    if check_id(data["Id"], Orders):
        return "Non-existent id or class"

    o = Orders.query.get(data["Id"])

    column_list = {
        "order_type": o.order_type,
        "descriptions": o.descriptions,
        "status": o.status,
        "serial_no": o.serial_no
    }

    if column in column_list.keys():
        column_list[column] = data["New_value"]
    else:
        return "Wrong column"
    return "Successfully updated"


if __name__ == "__main__":
    my_app.run()

