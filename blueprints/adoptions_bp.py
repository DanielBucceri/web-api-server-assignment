from flask import Blueprint, request
from init import db
from models.adoption import Adoption, one_adoption, many_adoptions, adoption_without_id
from models.user import User
from models.pet import Pet
from datetime import datetime

adoptions_bp = Blueprint('adoptions', __name__)

# READ ALL
@adoptions_bp.route('/adoptions', methods=['GET'])
def get_all_adoptions():
    adops = Adoption.query.all()
    return many_adoptions.dump(adops), 200

# READ ONE
@adoptions_bp.route('/adoptions/<int:adoption_id>', methods=['GET'])
def get_one_adoption(adoption_id):
    adp = Adoption.query.get(adoption_id)
    if adp:
        return one_adoption.dump(adp)
    return {"error": f"Adoption record with id {adoption_id} not found"}, 404


# CREATE
@adoptions_bp.route('/adoptions', methods=['POST'])
def create_adoption():
    data = adoption_without_id.load(request.json) #  load the model with the 
    user = User.query.get(data['user_id'])
    pet = Pet.query.get(data['pet_id'])
        
    if not user:
        return {"error": f"User with id {data['user_id']} not found"}, 404
    if not pet:
        return {"error": f"Pet with id {data['pet_id']} not found"}, 404
    if pet.is_adopted:
        return {"error": "Pet is already adopted"}, 400
    if pet.user_id == user.id:
        return {"error": "User already owns this pet"}, 400
    else:
        pet.user_id = user.id
        pet.is_adopted = "Adopted"

    new_adoption = Adoption(**data)
    db.session.add(new_adoption)
    db.session.commit()
    return one_adoption.dump(new_adoption), 201


# UPDATE is excluded as we do not want to update adoption records
# DELETE is exluded as we keep adoption records for historical purposes

