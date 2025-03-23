from flask import Blueprint, request
from init import db
from models.user import User, one_user, many_users, user_without_id
from models.address import Address

users_bp = Blueprint('users', __name__)

# READ ALL
@users_bp.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return many_users.dump(users), 200

# READ ONE
@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    user = User.query.get(user_id)
    if user:
        return one_user.dump(user), 200
    return {"error": f"User with id {user_id} not found"}, 404

# CREATE
@users_bp.route('/users', methods=['POST'])
def create_user():
    data = user_without_id.load(request.json)
    # Verify that the address exists if an address_id is provided
    if "address_id" in data:
        address = Address.query.get(data["address_id"])
        if not address:
            return {"error": f"Address with id {data['address_id']} not found"}, 404
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return one_user.dump(new_user), 201

# UPDATE
@users_bp.route('/users/<int:user_id>', methods=['PUT', 'PATCH'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": f"User with id {user_id} not found"}, 404
    data = user_without_id.load(request.json, partial=True)
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.email = data.get('email', user.email)
    user.phone = data.get('phone', user.phone)
    if 'address_id' in data:
        address = Address.query.get(data['address_id'])
        if not address:
            return {"error": f"Address with id {data['address_id']} not found"}, 404
        user.address_id = data['address_id']
    db.session.commit()
    return one_user.dump(user), 200

# DELETE
@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": f"User with id {user_id} not found"}, 404
    db.session.delete(user)
    db.session.commit()
    return {"message": "User deleted successfully"}, 200
