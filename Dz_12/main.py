from time import sleep
from flask import Flask
from Dz_10.orders_for_Dz_10 import *
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

my_app = Flask("my_app")


@my_app.route("/start/<string:id_list>", methods=['GET'])
def get_data_by_id(id_list):
    data = dict()
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = [pool.submit(get_data, i) for i in id_list.split()]

    for future in as_completed(results):
        data[f"Id:{future.result()[0]}"] = future.result()

    save_in_json(data)
    return data


def save_in_json(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def get_data(id_):
    sleep(2)
    return Orders.get_data_by_id(id_)["Order"][0]



if __name__ == "__main__":
    my_app.run(debug=True)

