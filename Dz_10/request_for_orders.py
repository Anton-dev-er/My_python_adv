from flask import Flask
from Dz_10.orders_for_Dz_10 import *
my_app = Flask("my_app")


@my_app.route("/Department/create_table")
def d_create_table():
    with conn, conn.cursor() as cursor:
        cursor.execute(DEPARTMENTS_TABLE)


@my_app.route("/Department/department_name/change_by_id/<string:value>/<int:id_>", methods=["PUT"])
def d_change_name_by_id(value, id_):
    old_value = Departments.get_data_by_id(id_)
    Departments.change_name_by_id(value, id_)
    return {"New value": Departments.get_data_by_id(id_),
            "Old value": old_value}


@my_app.route("/Department/get_data_by_id/<int:id_>", methods=["GET"])
def d_get_data_by_id(id_):
    return Departments.get_data_by_id(id_)


@my_app.route("/Department/delete_data_by_id/<int:id_>", methods=["DELETE"])
def d_delete_data_by_id(id_):
    Departments.delete_data_by_id(id_)
    return "Column was deleting"


@my_app.route("/Employee/create_table")
def e_create_table():
    with conn, conn.cursor() as cursor:
        cursor.execute(EMPLOYEES_TABLE)


@my_app.route("/Employee/fio/change_by_id/<string:value>/<int:id_>", methods=["PUT"])
def e_change_fio_by_id(value, id_):
    old_value = Employees.get_data_by_id(id_)
    Employees.change_fio_by_id(value, id_)
    return {"New value": Employees.get_data_by_id(id_),
            "Old value": old_value}


@my_app.route("/Employee/department_id/change_by_id/<int:value>/<int:id_>", methods=["PUT"])
def e_change_department_id_by_id(value, id_):
    old_value = Employees.get_data_by_id(id_)
    Employees.change_department_id_by_id(value, id_)
    return {"New value": Employees.get_data_by_id(id_),
            "Old value": old_value}


@my_app.route("/Employee/position/change_by_id/<string:value>/<int:id_>", methods=["PUT"])
def e_change_position_by_id(value, id_):
    old_value = Employees.get_data_by_id(id_)
    Employees.change_position_by_id(value, id_)
    return {"New value": Employees.get_data_by_id(id_),
            "Old value": old_value}


@my_app.route("/Employee/get_data_by_id/<int:id_>", methods=["GET"])
def e_get_data_by_id(id_):
    return Employees.get_data_by_id(id_)


@my_app.route("/Employee/delete_data_by_id/<int:id_>", methods=["DELETE"])
def e_delete_data_by_id(id_):
    Departments.delete_data_by_id(id_)
    return "Column was deleting"


@my_app.route("/Order/create_table")
def o_create_table():
    with conn, conn.cursor() as cursor:
        cursor.execute(ORDERS_TABLE)


@my_app.route("/Order/order_type/change_by_id/<string:value>/<int:id_>", methods=["PUT"])
def o_change_creator_id_by_id(value, id_):
    old_value = Orders.get_data_by_id(id_)
    Orders.change_order_type_by_id(value, id_)
    return {"New value": Orders.get_data_by_id(id_),
            "Old value": old_value}


@my_app.route("/Order/description/change_by_id/<string:value>/<int:id_>", methods=["PUT"])
def o_change_description_by_id(value, id_):
    old_value = Orders.get_data_by_id(id_)
    Orders.change_description_by_id(value, id_)
    return {"New value": Orders.get_data_by_id(id_),
            "Old value": old_value}


@my_app.route("/Order/status/change_by_id/<string:value>/<int:id_>", methods=["PUT"])
def o_change_status_by_id(value, id_):
    old_value = Orders.get_data_by_id(id_)
    Orders.change_status_by_id(value, id_)
    return {"New value": Orders.get_data_by_id(id_),
            "Old value": old_value}


@my_app.route("/Order/serial_no/change_by_id/<int:value>/<int:id_>", methods=["PUT"])
def o_change_serial_no_by_id(value, id_):
    old_value = Orders.get_data_by_id(id_)
    Orders.change_serial_no_by_id(value, id_)
    return {"New value": Orders.get_data_by_id(id_),
            "Old value": old_value}


@my_app.route("/Order/creator_id/change_by_id/<int:value>/<int:id_>", methods=["PUT"])
def o_change_serial_no_by_id(value, id_):
    old_value = Orders.get_data_by_id(id_)
    Orders.change_creator_id_by_id(value, id_)
    return {"New value": Orders.get_data_by_id(id_),
            "Old value": old_value}


@my_app.route("/Orders/get_data_by_id/<int:id_>", methods=["GET"])
def o_get_data_by_id(id_):
    return Orders.get_data_by_id(id_)


@my_app.route("/Orders/delete_data_by_id/<int:id_>", methods=["DELETE"])
def o_delete_data_by_id(id_):
    Orders.delete_data_by_id(id_)
    return "Column was deleting"


if __name__ == "__main__":
    my_app.run(debug=True)