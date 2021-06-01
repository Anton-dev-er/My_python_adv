from datetime import datetime
import psycopg2
from psycopg2 import sql

orders = [("Friday", 'order_type_1', 'Active', 12344, 1),
          ("Friday", 'order_type_2', 'Active', 45745, 1),
          ("Sunday", 'order_type_3', 'Closed', 45657, 2),
          ("Sunday", 'order_type_4', 'Active', 56777, 2),
          ("Sunday", 'order_type_4', 'Closed', 78978, 3)]

employees = [("Косенко Руслан Віталійвоч", "Сварщик", 1),
             ("Бмшко Микита Андрійович", "Сварщик", 1),
             ("Харлан Володимир Миколайович", "Механик", 3),
             ("Харлан Володимир Миколайович 2", "Механик", 3),
             ("Подиман Григорій Сергійович", "Програмист", 5),
             ("Телестакова Вікторія Вікторівна", "Менеджер", 2),
             ("Кто еще 1", "Програмист", 5),
             ("Кто еще 2", "Програмист", 5),
             ("Кто еще 3", "Програмист", 5),
             ("Кто еще 4", "Програмист", 5)]

departments = ["department_1",
               "department_2",
               "department_3",
               "department_4",
               "department_5"]

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

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="Plisiukk_11",
    host="localhost",
    port="5432"
)


def insert_into_table(data_for_insert, table):
    with conn, conn.cursor() as cursor:
        for i in table:
            cursor.execute(data_for_insert, i)


def insert_into_departments (data_for_insert, table):
    with conn, conn.cursor() as cursor:
        for i in table:
            cursor.execute(data_for_insert, [i])


def show_table(SELECT_QUERY):
    with conn, conn.cursor() as cursor:
        cursor.execute(SELECT_QUERY)
        print(cursor.fetchall())


def create_table(table):
    with conn, conn.cursor() as cursor:
        cursor.execute(table)


def  get_list_by_employees_and_departments():
    with conn, conn.cursor() as cursor:
        cursor.execute("""SELECT fio, department_name 
        FROM employees 
        LEFT JOIN departments 
        ON departments.department_id = employees.department_id """)
        for i in cursor:
            print(i)


def get_days_and_count_orders_by_status(status):
    with conn, conn.cursor() as cursor:
        cursor.execute(f""" SELECT created_dt, count(status)
                            FROM orders o 
                            WHERE status = '{status}'
                            GROUP BY (created_dt) """)
        for i in cursor:
            print(i)


def get_orders_in_a_certain_status_and_employee_by_status(status):
    with conn, conn.cursor() as cursor:
        cursor.execute(f""" SELECT fio, status, created_dt 
                            FROM orders o
                            LEFT JOIN employees e 
                            ON creator_id = employee_id
                            WHERE status = '{status}'""")
        for i in cursor:
            print(i)


def main():
    SELECT_QUERY_d = """SELECT * FROM departments"""
    SELECT_QUERY_o = """SELECT * FROM orders"""
    SELECT_QUERY_e = """SELECT * FROM employees"""
    insert_in_orders = sql.SQL("""INSERT INTO orders (created_dt, order_type, status, serial_no, creator_id) 
                                VALUES (%s, %s, %s, %s, %s)""")
    insert_in_departments = sql.SQL("""INSERT INTO departments(department_name) 
                                VALUES (%s)""")
    insert_in_employees = sql.SQL("""INSERT INTO employees(fio, position_, department_id) 
                                VALUES (%s, %s, %s)""")

    # create_table(DEPARTMENTS_TABLE)
    # create_table(EMPLOYEES_TABLE)
    # create_table(ORDERS_TABLE)
    #
    # insert_into_departments(insert_in_departments, departments)
    # insert_into_table(insert_in_employees, employees)
    # insert_into_table(insert_in_orders, orders)
    #
    # show_table(SELECT_QUERY_d)
    # show_table(SELECT_QUERY_o)
    # show_table(SELECT_QUERY_e)

    # - 1
    # get_orders_in_a_certain_status_and_employee_by_status('Active')

    # - 2
    # get_list_by_employees_and_departments()

    # - 3
    # get_days_and_count_orders_by_status('Closed')
    # get_days_and_count_orders_by_status('Active')



main()
