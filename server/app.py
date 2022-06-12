from flask import Flask, jsonify
from flask_cors import CORS
import os
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/users', methods=['GET'])
def all_books():
    return jsonify({
        'status': 'success',
        'users': USERS
    })


USERS = []

for filename in os.listdir("usersData"):
    with open(os.path.join("usersData", filename), 'r') as f:
        jsonObj = json.load(f)
        USERS.append(jsonObj)

if __name__ == '__main__':
    app.run()
