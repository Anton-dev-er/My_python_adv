from psycopg2 import connect
from envparse import Env
from datetime import date, datetime
from abc import ABC, abstractmethod


env = Env()
CONN_STRING = env.str("CONN")
conn = connect(CONN_STRING)


class DataRequiredException(Exception):
    pass


class Departments():
    __CREATE_DEPARTMENTS_QUERY = """INSERT INTO departments (department_name) VALUES (%s) RETURNING department_id"""
    __DELETE_DEPARTMENTS_QUERY = """DELETE FROM departments WHERE department_id = %s"""

    def __init__(self, department_name: str, department_id=None):
        self.__department_name = department_name
        self.__department_id = department_id

    @property
    def department_id(self):
        return self.__department_id

    @department_id.setter
    def department_id(self, value):
        self.__department_id = value

    @staticmethod
    def get_data_by_column(*args):
        with conn, conn.cursor() as cursor:
            cursor.execute(f"""SELECT {",".join(args) if args != () else "*"} FROM departments""")
            return {"Department": cursor.fetchall()}

    @staticmethod
    def get_data_by_id(id_):
        with conn, conn.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM departments WHERE department_id={id_}""")
            return {"Department": cursor.fetchall()}

    def save(self):
        with conn, conn.cursor() as cursor:
            cursor.execute(self.__class__.__CREATE_DEPARTMENTS_QUERY, [self.__department_name])
            self.__department_id = cursor.fetchone()[0]
            return {"department_id": self.__department_id}

    @classmethod
    def delete_data_by_id(cls, id_):
        with conn, conn.cursor() as cursor:
            cursor.execute(cls.__DELETE_DEPARTMENTS_QUERY, [f"{id_}"])
            raise

    @staticmethod
    def __change_value(value, id_):
        query = """UPDATE departments SET department_name = %s, updated_dt = %s WHERE department_id = %s"""
        with conn, conn.cursor() as cursor:
            cursor.execute(query, (value, datetime.now(), id_))

    @classmethod
    def change_name_by_id(cls, new_department_name: str, id_column: int):
        cls.__change_value(new_department_name, id_column)


class Employees():
    __CREATE_EMPLOYEES_QUERY = """INSERT INTO employees (fio, position_, department_id) 
                                VALUES (%s, %s, %s) 
                                RETURNING employee_id"""
    __DELETE_EMPLOYEES_QUERY = """DELETE FROM employees WHERE employee_id = %s"""

    def __init__(self, fio, position_, department_id, updated_dt=None, employee_id=None):
        self.__fio = fio
        self.__position_ = position_
        self.__department_id = department_id
        self.__updated_dt = updated_dt
        self.__employee_id = employee_id

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        self.__employee_id = value

    @staticmethod
    def get_data_by_column(*args):
        with conn, conn.cursor() as cursor:
            cursor.execute(f"""SELECT {",".join(args) if args != () else "*"} FROM employees""")
            return cursor.fetchall()

    @staticmethod
    def get_data_by_id(id_):
        with conn, conn.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM employees where employee_id={id_}""")
            return {"Employees": cursor.fetchall()}

    def save(self):
        with conn, conn.cursor() as cursor:
            cursor.execute(self.__class__.__CREATE_EMPLOYEES_QUERY, [self.__fio, self.__position_, self.__department_id])
            self.__employee_id = cursor.fetchone()[0]
            return {"employee_id": self.__employee_id}

    def delete_data_by_id(self):
        with conn, conn.cursor() as cursor:
            if not self.__employee_id:
                raise DataRequiredException("Employee_id param is required for deleting!")
            else:
                cursor.execute(self.__class__.__DELETE_EMPLOYEES_QUERY, [f"{self.__employee_id}"])

    @staticmethod
    def __change_value(value, id_, column):
        query = f"""UPDATE employees SET {column} = %s, updated_dt = %s WHERE employee_id = %s"""
        with conn, conn.cursor() as cursor:
            cursor.execute(query, [value, datetime.now(), id_])

    @classmethod
    def change_fio_by_id(cls, new_fio: str, id_column: int):
        cls.__change_value(new_fio, id_column, "fio")

    @classmethod
    def change_position_by_id(cls, new_position: str, id_column: int):
        cls.__change_value(new_position, id_column, "position_")

    @classmethod
    def change_department_id_by_id(cls, new_department_id: int, id_column: int):
        cls.__change_value(new_department_id, id_column, "department_id")


class Orders():
    __CREATE_ORDER_QUERY = """INSERT INTO orders (created_dt, order_type, status, serial_no, creator_id, description) 
                           VALUES (%s, %s, %s, %s, %s, %s) RETURNING order_id"""
    __DELETE_EMPLOYEES_QUERY = """DELETE FROM orders WHERE order_id = %s"""

    def __init__(self, order_type: str, status: str, serial_no: int, creator_id: int, description=None, order_id=None):
        self.__created_dt = date.today()
        self.__order_type = order_type
        self.__status = status
        self.__serial_no = serial_no
        self.__creator_id = creator_id
        self.__description = description
        self.__order_id = order_id

    @property
    def order_id(self):
        return self.__order_id

    @order_id.setter
    def order_id(self, value):
        self.__order_id = value

    @staticmethod
    def get_data_by_column(*args):
        with conn, conn.cursor() as cursor:
            cursor.execute(f"""SELECT {",".join(args) if args != () else "*"} FROM orders""")
            return cursor.fetchall()

    @staticmethod
    def get_data_by_id(id_):
        with conn, conn.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM employees where order_id={id_}""")
            return {"Order": cursor.fetchall()}

    def save(self):
        with conn, conn.cursor() as cursor:
            cursor.execute(self.__class__.__CREATE_ORDER_QUERY, (self.__created_dt, self.__order_type, self.__status,
                                                              self.__serial_no, self.__creator_id, self.__description))
            self.__order_id = cursor.fetchone()[0]
            return {"order_id":  self.__order_id}

    def delete_data_by_id(self):
        with conn, conn.cursor() as cur:
            if not self.__order_id:
                raise DataRequiredException("Order_id param is required for deleting!")
            else:
                cur.execute(self.__class__.__DELETE_EMPLOYEES_QUERY, [f"{self.__order_id}"])

    @staticmethod
    def __change_value(value, id_, column):
        query = f"""UPDATE orders SET {column} = %s, updated_dt = %s WHERE order_id = %s"""
        with conn, conn.cursor() as cursor:
            cursor.execute(query, [value, datetime.now(), id_])

    @classmethod
    def change_order_type_by_id(cls, new_order_type: str, id_column: int):
        cls.__change_value(new_order_type, id_column, "order_type")

    @classmethod
    def change_description_by_id(cls, new_description: str, id_column: int):
        cls.__change_value(new_description, id_column, "description")

    @classmethod
    def change_status_by_id(cls, status: str, id_column: int):
        cls.__change_value(status, id_column, "status")

    @classmethod
    def change_serial_no_by_id(cls, new_serial_no: int, id_column: int):
        cls.__change_value(new_serial_no, id_column, "serial_no")

    @classmethod
    def change_creator_id_by_id(cls, new_creator_id: int, id_column: int):
        cls.__change_value(new_creator_id, id_column, "creator_id")


def main():
    # d1 = Departments("DPR_pr")
    # d1.save()
    #
    # e1 = Employees("Anton", "Programer", 3)
    # e1.save()
    #
    # o1 = Orders("Non_type", "Active", 23534, 3, "My order")
    # o1.save()

    # o1.delete_data_by_id()
    # e1.delete_data_by_id()
    # d1.delete_data_by_id()

    # Departments.change_name_by_id("NEW name", 1)

    # Employees.change_fio_by_id("New fio", 1)
    # Employees.change_position_by_id("New pos", 1)
    # Employees.change_department_id_by_id(3, 1)

    # Orders.change_order_type_by_id("Active", 2)
    # Orders.change_description_by_id("New desc", 2)
    # Orders.change_status_by_id("Closed", 2)
    # Orders.change_serial_no_by_id(42142, 2)
    # Orders.change_creator_id_by_id(3, 2)

    print(Departments.get_data_by_column())
    # Employees.get_data_by_column()
    # Orders.get_data_by_column()
    pass

DEPARTMENTS_TABLE = """
CREATE TABLE IF NOT EXISTS departments (
    department_id SERIAL PRIMARY KEY,
    department_name TEXT NOT NULL );
"""

EMPLOYEES_TABLE = """
CREATE TABLE IF NOT EXISTS employees (
    employee_id SERIAL PRIMARY KEY,
    fio TEXT NOT NULL,
    position_ TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments (department_id) );
"""

ORDERS_TABLE = """
CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    created_dt TEXT NOT NULL,
    updated_dt TEXT,
    order_type TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL,
    serial_no INTEGER NOT NULL,
    creator_id INTEGER NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES employees (employee_id) );
"""


main()

