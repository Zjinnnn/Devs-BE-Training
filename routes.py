from flask import Blueprint, jsonify, request
from pymongo import MongoClient

# Connect to MongoDB
cluster = MongoClient("mongodb+srv://devsbe:U9MJGWLZXS885FqS@cluster0.6capukj.mongodb.net/")
db = cluster["db1"]
collection = db["as2"]

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return "Hello Backend"


@main.route('/about_me', methods=['GET','POST'])
def about_me():
    try:
        if request.method == "POST":
            print("Received POST Request")
            data = request.get_json()
            collection.insert_one(data)
            return jsonify({"Msg": "Data saved successfully"}), 201
        if request.method == "GET":
            name = request.args.get('name')
            data = collection.find_one({"Name": name})
            if data:
                # Convert ObjectId to string
                data['_id'] = str(data['_id'])
                return jsonify(data), 200
            else:
                return jsonify({"msg": "Data not found"}), 404
    except Exception as e:
        print(f"Error: {e}")
        return "Connection Error", 404
