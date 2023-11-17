from flask import Blueprint, jsonify, request

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return "Hello Backend"

@main.route('/about_me', methods=['POST'])
def about_me():
    try:
        if request.method == "POST":
            print("Received POST Request")
            data = request.get_json()
            return jsonify(data), 200
    except Exception as e:
        print(f"Error: {e}")
        return "Can't add", 404
