import json
import datetime
import os.path

# def set_time_of_creation(cls):
#     def inner():
#         with open("new_file.json", "r+", encoding="utf-8") as f:
#             f.
#     return inner
#
#
# @set_time_of_creation
# class Test:
#     pass
#
# t = Test()
# t1 = Test()
# t2 = Test()
# t3 = Test()
# t4 = Test()


def write_data(cls):
    def inner():
        if not os.path.exists("new_file.json"):
            with open("new_file.json", "x", encoding="utf-8") as f:
                f.write("{}")

        with open("new_file.json", "r+") as f:
            data = json.load(f)
            data[f"{id(cls())}"] = {"time": f"{datetime.datetime.now()}", "data": f"{cls()}"}
            data = json.dumps(data, indent=4)
            f.seek(0)
            f.write(data)
    return inner


@write_data
class Test:
    pass

@write_data
class OtherClass:
    pass


t1 = Test()
t2 = Test()
t3 = OtherClass()
t4 = OtherClass()
