from init import db, ma
from sqlalchemy.orm import relationship
from marshmallow import fields, validate
 
class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    species = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100))
    color = db.Column(db.String(100), nullable=False)
    adoption_status = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100))
    image = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship("User", back_populates="pets")
    
class PetSchema(ma.Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    species = fields.String(required=True, validate=validate.Length(min=1))
    
    class Meta:
        fields = ("id", "name", "age", "breed", "color", "adoption_status", "description", "image")
    
one_pet = PetSchema()
many_pets = PetSchema(many=True)
pet_without_id = PetSchema(exclude=["id"])

    