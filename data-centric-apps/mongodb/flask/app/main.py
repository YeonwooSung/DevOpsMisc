import os
from flask import Flask, jsonify, request
import pymongo


app = Flask(__name__)

mongo_url = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@localhost:27017/'
mongo = pymongo.MongoClient(mongo_url)
db = mongo['flaskdb']


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/todo', methods=['POST'])
def createTodo():
    data = request.get_json(force=True)
    item = {
        'todo': data['todo']
    }
    db['todo'].insert_one(item)

    return jsonify(
        status=True,
        message='To-do saved successfully!'
    ), 200
