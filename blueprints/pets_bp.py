from flask import Blueprint, request
from init import db
from models.pet import Pet, one_pet, many_pets, pet_without_id

pets_bp = Blueprint('pets', __name__)

# READ ALL
@pets_bp.route('/pets', methods=['GET'])
def get_all_pets():
    pets = Pet.query.all()
    return many_pets.dump(pets), 200

# READ ONE
@pets_bp.route('/pets/<int:pet_id>', methods=['GET'])
def get_one_pet(pet_id):
    pet = Pet.query.get(pet_id)
    if pet:
        return one_pet.dump(pet), 200
    return {"error": f"Pet with id {pet_id} not found"}, 404

# CREATE
@pets_bp.route('/pets', methods=['POST'])
def create_pet():
    data = pet_without_id.load(request.json)
    new_pet = Pet(**data)
    db.session.add(new_pet)
    db.session.commit()
    return one_pet.dump(new_pet), 201

# UPDATE
@pets_bp.route('/pets/<int:pet_id>', methods=['PUT', 'PATCH'])
def update_pet(pet_id):
    pet = Pet.query.get(pet_id)
    if not pet:
        return {"error": f"Pet with id {pet_id} not found"}, 404

    data = pet_without_id.load(request.json, partial=True)

    # Update regular fields
    pet.name = data.get('name', pet.name)
    pet.age = data.get('age', pet.age)
    pet.species = data.get('species', pet.species)
    pet.breed = data.get('breed', pet.breed)
    pet.color = data.get('color', pet.color)
    pet.description = data.get('description', pet.description)
    pet.image = data.get('image', pet.image)

    db.session.commit()
    return one_pet.dump(pet), 200


# DELETE
@pets_bp.route('/pets/<int:pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    pet = Pet.query.get(pet_id)
    if not pet:
        return {"error": f"Pet with id {pet_id} not found"}, 404
    db.session.delete(pet)
    db.session.commit()
    return {"message": "Pet deleted successfully"}, 200

# remove owners by releasing the pet
@pets_bp.route('/pets/<int:pet_id>/release', methods=['POST'])
def release_pet(pet_id):
    pet = Pet.query.get(pet_id)
    if not pet:
        return {"error": f"Pet with id {pet_id} not found"}, 404
    if not pet.is_adopted or pet.user_id is None:
        return {"error": "Pet is not currently adopted"}, 400

    # Unassign owner and mark as available
    pet.user_id = None
    pet.is_adopted = False
    db.session.commit()
    return {"message": f"Pet {pet.name} is now available for adoption again."}, 200
