from flask import Blueprint, request
from init import db
from models.adoption import Adoption, one_adoption, many_adoptions, adoption_without_id
from models.user import User
from models.pet import Pet

adoptions_bp = Blueprint('adoptions', __name__)

# READ ALL
@adoptions_bp.route('/adoptions')
def get_all_adoptions():
    adops = Adoption.query.all()
    return many_adoptions.dump(adops), 200

# READ ONE
@adoptions_bp.route('/adoptions/<int:adoption_id>')
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
    if not user or not pet:
        return {"error": "User or Pet not found"}, 404
    elif pet.user_id == user.id:
        return {"error": "User already linked to pet"}, 400
    else:
        pet.user_id = user.id
        pet.adoption_status = "Adopted"

    new_adoption = Adoption(**data)
    db.session.add(new_adoption)
    db.session.commit()
    return one_adoption.dump(new_adoption), 201

# UPDATE
@adoptions_bp.route('/adoptions/<int:adoption_id>', methods=['PUT','PATCH'])
def update_adoption(adoption_id):
    adp = Adoption.query.get(adoption_id)
    if not adp:
        return {"error": f"Adoption record with id {adoption_id} not found"}, 404

    data = adoption_without_id.load(request.json , partial=True)
    adp.user_id = data.get('user_id', adp.user_id)
    adp.pet_id = data.get('pet_id', adp.pet_id)
    adp.notes = data.get('notes', adp.notes)
    db.session.commit()
    return one_adoption.dump(adp), 200
