from flask import Blueprint, jsonify, request
from ..models.user import User

users_bp = Blueprint('users', __name__)

# Stocke la donnée en mémoire (TEMPORAIRE!)
users = []
user_id_ctr = 1

@users_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify([user.to_dict() for user in users])

@users_bp.route('/users', methods=['POST'])
def create_users():
    global user_id_ctr
    data = request.get_json()

    if not data or 'username' not in data: 
        return jsonify({"error": "username is required is request body!"}), 400

    user = User(username=data['username'])
    user.id = user_id_ctr
    user_id_ctr += 1

    users.append(user)
    return jsonify(user.to_dict()), 201
