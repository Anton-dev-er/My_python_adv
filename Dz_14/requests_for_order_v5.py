import json
from flask import Flask, request
app = Flask('app')


@app.route('/main', methods=['POST'])
def parse_request():
    data = request.data
    print(data)
    return "OK"

app.run()