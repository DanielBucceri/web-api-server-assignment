from flask import Blueprint, request
from init import db
from models.user import User
from models.address import Address, one_address, address_without_id

addresses_bp = Blueprint('addresses', __name__)

# CREATE
@addresses_bp.route('/addresses', methods=['POST'])
def create_address():
    data = address_without_id.load(request.json)
    new_addr = Address(**data)
    db.session.add(new_addr)
    db.session.commit()
    return address_without_id.dump(new_addr), 201

# UPDATE
@addresses_bp.route('/addresses/<int:address_id>', methods=['PUT','PATCH'])
def update_address(address_id):
    addr = Address.query.get(address_id)
    if not addr:
        return {"error": f"Address with id {address_id} not found"}, 404

    data = address_without_id.load(request.json, partial=True)
    addr.street = data.get('street', addr.street)
    addr.city = data.get('city', addr.city)
    addr.state = data.get('state', addr.state)
    addr.postcode = data.get('postcode', addr.postcode)
    db.session.commit()
    return one_address.dump(addr), 200

# DELETE
@addresses_bp.route('/addresses/<int:address_id>', methods=['DELETE'])
def delete_address(address_id):
    addr = Address.query.get(address_id)
    if not addr:
        return {"error": f"Address with id {address_id} not found"}, 404
    db.session.delete(addr)
    db.session.commit()
    return {"message": "Address deleted successfully"}, 200
