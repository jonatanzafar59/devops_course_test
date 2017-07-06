from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def print_hello():
    my_param = request.json
    return json.dumps(my_param)

app.run(host='0.0.0.0', port=5555)


