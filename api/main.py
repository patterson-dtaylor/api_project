from flask import Flask, jsonify, request
from flask.testing import FlaskClient
import api_modules.users_controller as db_controller
import api_modules.api_operations as api_operations
from data.db import create_tables

app = Flask(__name__)

# def create_test_client(app):
#     return app.test_client()

@app.route('/api/healthchecker')
def root():
    return jsonify({
        'status': 'healthy'
    })

@app.route('/users', methods=["GET"])
def get_users():
    users = db_controller.get_users()
    return jsonify(users)

@app.route("/user", methods=["POST"])
def insert_user():
    user_details = request.get_json()
    name = user_details["name"]
    username = user_details["username"]
    if not api_operations.is_username_valid(username):
        return jsonify({
            'status': '422',
            'res': 'failure',
            'error': 'Invalid username format. Please enter a valid username with 4-16 Alpha Numeric Characters with no Special Characters'
        })
    email = user_details["email"]
    if not api_operations.is_email_valid(email):
        return jsonify({
            'status': '422',
            'res': 'failure',
            'error': 'Invalid email format. Please enter a valid email address'
        })
    db_controller.insert_user(name, username, email)
    return {"Status": "Success", "User": user_details}


@app.route("/user/<id>", methods=["PUT"])
def update_user(id):
    user_details = request.get_json()
    name = user_details["name"]
    username = user_details["username"]
    if not api_operations.is_username_valid(username):
        return jsonify({
            'status': '422',
            'res': 'failure',
            'error': 'Invalid username format. Please enter a valid username with 4-16 Alpha Numeric Characters with no Special Characters'
        })
    email = user_details["email"]
    if not api_operations.is_email_valid(email):
        return jsonify({
            'status': '422',
            'res': 'failure',
            'error': 'Invalid email format. Please enter a valid email address'
        })
    db_controller.update_user(id, name, username, email)
    return {"Status": "Success", "User": user_details}

@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    db_controller.delete_user(id)
    return {"Status": "Success", "Message": "User deleted successfully"}


@app.route("/user/<id>", methods=["GET"])
def get_user_by_id(id):
    user = db_controller.get_by_id(id)
    return jsonify(user)

if __name__ == "__main__":
    create_tables()
    app.run(host='0.0.0.0', port=8000, debug=True)