from datetime import datetime
import mongoengine as me

me.connect("HW_8")


class Departments(me.Document):
    departments_name = me.StringField(required=True)
    created_dt = me.DateTimeField()

    def save_new_record(self, *args, **kwargs):
        self.created_dt = datetime.now()
        return self.save(*args, **kwargs)

    def delete_new_record(self):
        self.delete()

    def change_record(self, field: str, new_value):
        fields = {"departments_name": 0}
        if field in fields:
            if fields[field] == 0:
                self.departments_name = new_value
            else:
                print("Wrong field")

    def __str__(self):
        return f"Departments name: {self.departments_name}"


class Employee(me.Document):
    fio = me.StringField(required=True)
    position = me.StringField(required=True)
    department_id = me.ReferenceField(Departments, required=True)
    created_dt = me.DateTimeField()

    def save_new_record(self, *args, **kwargs):
        self.created_dt = datetime.now()
        return self.save(*args, **kwargs)

    def delete_new_record(self):
        self.delete()

    def change_record(self, field: str, new_value):
        fields = {"position": 0, "fio": 1}
        if field in fields:
            if fields[field] == 0:
                self.position = new_value
            elif fields[field] == 1:
                self.fio = new_value
            else:
                print("Wrong field")

    def __str__(self):
        return f"Fio: {self.fio}, Positions: {self.position}, Create dt: {self.created_dt}"


class Orders(me.Document):
    created_dt = me.DateTimeField()
    order_type = me.StringField(required=True)
    descriptions = me.StringField()
    status = me.StringField(required=True)
    serial_no = me.IntField(required=True)
    creator_id = me.ReferenceField(Employee, required=True)

    def save_new_record(self, *args, **kwargs):
        self.created_dt = datetime.now()
        return self.save(*args, **kwargs)

    def delete_new_record(self):
        self.delete()

    def change_record(self, field: str, new_value):
        fields = {"order_type": 0,
                  "descriptions": 1,
                  "status": 2,
                  "serial_no": 3}
        if field in fields:
            if fields[field] == 0:
                self.order_type = new_value
            elif fields[field] == 1:
                self.descriptions = new_value
            elif fields[field] == 2:
                self.status = new_value
            elif fields[field] == 3:
                self.serial_no = new_value
            else:
                print("Wrong field")

    def __str__(self):
        return f"Created dt: {self.created_dt}" \
               f"Order type: {self.order_type}" \
               f"Descriptions: {self.descriptions}" \
               f"Status: {self.status}" \
               f"Serial Number {self.serial_no}"


d1 = Departments(departments_name="My name")
e1 = Employee(fio="Антон", position="Pos", department_id=d1)
o1 = Orders(order_type="some type", status="Active", serial_no=12445, creator_id=e1)
d1.save_new_record()
print(e1.save_new_record())
o1.save_new_record()
