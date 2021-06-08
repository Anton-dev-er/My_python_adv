from pprint import pprint
from psycopg2 import connect
from envparse import Env
from datetime import date, datetime
from abc import ABC, abstractmethod
from os import path
import json


env = Env()
CONN_STRING = env.str("CONN")
conn = connect(CONN_STRING)


class DataRequiredException(Exception):
    pass


class BaseModel(ABC):
    @abstractmethod
    def get_data_by_column(self, *args):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def delete_data_by_id(self):
        pass


class Departments(BaseModel):
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
            pprint(cursor.fetchall())

    def save(self):
        with conn, conn.cursor() as cursor:
            cursor.execute(self.__class__.__CREATE_DEPARTMENTS_QUERY, [self.__department_name])
            self.__department_id = cursor.fetchone()[0]
            return {"department_id": self.__department_id}

    def delete_data_by_id(self):
        with conn, conn.cursor() as cursor:
            if not self.__department_id:
                raise DataRequiredException("Department_id param is required for deleting!")
            else:
                cursor.execute(self.__class__.__DELETE_DEPARTMENTS_QUERY, [f"{self.__department_id}"])

    @staticmethod
    def __change_value(value, id_):
        query = """UPDATE departments SET department_name = %s, updated_dt = %s WHERE department_id = %s"""
        with conn, conn.cursor() as cursor:
            cursor.execute(query, (value, datetime.now(), id_))

    @classmethod
    def change_name_by_id(cls, new_department_name: str, id_column: int):
        cls.__change_value(new_department_name, id_column)

    def save_in_json(self):
        if self.__department_id is None:
            print("ID не может быть None")
        else:
            if not path.exists(f"Departments/{self.__department_id}.json"):
                with open(f"Departments/{self.__department_id}.json", "x", encoding="utf-8") as f:
                    f.write("{}")

            with open(f"Departments/{self.__department_id}.json", "w") as f:
                data = self.__show_data()
                data["Time of creation"] = f"{datetime.now()}"
                pprint(data)
                f.write(json.dumps(data, indent=4))

    def __show_data(self):
        id_ = self.__department_id
        if id_ is None:
            id_ = "Id будет показано после сохранения"
        return {"Name": self.__department_name, "ID": id_}

    def __str__(self):
        return self.__show_data()

    def __repr__(self):
        return self.__show_data()


class Employees(BaseModel):
    __CREATE_EMPLOYEES_QUERY = """INSERT INTO employees (fio, position_, department_id) 
                                VALUES (%s, %s, %s) 
                                RETURNING employee_id"""
    __DELETE_EMPLOYEES_QUERY = """DELETE FROM employees WHERE employee_id = %s"""

    def __init__(self, fio, position_, department_id, employee_id=None):
        self.__fio = fio
        self.__position_ = position_
        self.__department_id = department_id
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
            pprint(cursor.fetchall())

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

    def __show_data(self):
        id_ = self.__employee_id
        if id_ is None:
            id_ = "Id будет показано после сохранения"
        return {"Fio": self.__fio, "Positions": self.__position_, "Department ID": self.__department_id,
                "Employee ID": id_}

    def save_in_json(self):
        if self.__employee_id is None:
            print("ID не может быть None")
        else:
            if not path.exists(f"Employee/{self.__employee_id}.json"):
                with open(f"Employee/{self.__employee_id}.json", "x", encoding="utf-8") as f:
                    f.write("{}")

            with open(f"Employee/{self.__employee_id}.json", "w") as f:
                data = self.__show_data()
                data["Time of creation"] = f"{datetime.now()}"
                pprint(data)
                f.write(json.dumps(data, indent=4))

    def __str__(self):
        return self.__show_data()

    def __repr__(self):
        return self.__show_data()


class Orders(BaseModel):
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
            pprint(cursor.fetchall())

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
    def change_data_by_id_and_column(column: str, new_value, id_: int):
        query = f"""UPDATE orders SET {column} = %s, updated_dt = %s WHERE order_id = %s"""
        with conn, conn.cursor() as cursor:
            cursor.execute(query, [new_value, datetime.now(), id_])

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

    def __show_data(self):
        id_ = self.__order_id
        if id_ is None:
            id_ = "Id будет показано после сохранения"
        return {"Order type": self.__order_type, "Status": self.__status,
                "Serial number": self.__serial_no, "Creator ID": self.__creator_id,
                "Descriptions": self.__description, "Order ID": id_}

    def save_in_json(self):
        if self.__order_id is None:
            print("ID не может быть None")
        else:
            if not path.exists(f"Orders/{self.__order_id}.json"):
                with open(f"Orders/{self.__order_id}.json", "x", encoding="utf-8") as f:
                    f.write("{}")

            with open(f"Orders/{self.__order_id}.json", "w") as f:
                data = self.__show_data()
                data["Time of creation"] = f"{datetime.now()}"
                pprint(data)
                f.write(json.dumps(data, indent=4))

    def __str__(self):
        return self.__show_data()

    def __repr__(self):
        return self.__show_data()


def main():
    d = Departments("name")
    d.save()
    d.save_in_json()

    e = Employees("fio", "pos", 2)
    e.save()
    e.save_in_json()

    o = Orders("type", "Status", 1241, 2, "sadasd")
    o.save()
    o.save_in_json()


main()
