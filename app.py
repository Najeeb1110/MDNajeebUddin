from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb+srv://Hunter:14300@11.jdkrn.mongodb.net/?retryWrites=true&w=majority&appName=11")
db = client.crud_db
collection = db.student

def convert_to_json(user):
    user["_id"] = str(user["_id"])
    return user


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = {
        "name": data['name'],
        "email": data['email']
    }
    result = collection.insert_one(new_user)
    return jsonify({"message": "User added", "id": str(result.inserted_id)}), 201

@app.route('/get_users', methods=['GET'])
def get_users():
    users = collection.find()
    users_list = [convert_to_json(user) for user in users]
    return jsonify(users_list), 200

@app.route('/get_user/<id>', methods=['GET'])
def get_user(id):
    user = collection.find_one({"_id": ObjectId(id)})
    if user:
        return jsonify(convert_to_json(user)), 200
    else:
        return jsonify({"message": "User not found"}), 404


@app.route('/update_user/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    updated_user = {
        "name": data['name'],
        "email": data['email']
    }
    result = collection.update_one({"_id": ObjectId(id)}, {"$set": updated_user})
    if result.matched_count > 0:
        return jsonify({"message": "User updated"}), 200
    else:
        return jsonify({"message": "User not found"}), 404
    
@app.route('/delete_user/<id>', methods=['DELETE'])
def delete_user(id):
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count > 0:
        return jsonify({"message": "User deleted"}), 200
    else:
        return jsonify({"message": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
