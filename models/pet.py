from init import db, ma
from sqlalchemy.orm import relationship
from marshmallow import fields, validate
from models.user import User, UserSchema

class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    species = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100))
    color = db.Column(db.String(100), nullable=False)
    is_adopted = db.Column(db.Boolean, default=False, nullable=False)
    description = db.Column(db.String(100))
    image = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship("User", back_populates="pets")


# Base schema for Pet (used for list views and input validation)
class PetSchema(ma.Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    species = fields.String(required=True, validate=validate.Length(min=1))
    
    class Meta:
        fields = ("id", "name", "age", "breed", "color", "is_adopted", "description", "image", "user_id")


# chema for a single pet includeing nested user info
class PetDetailSchema(PetSchema):
    user = fields.Nested(UserSchema(only=("id", "first_name", "last_name", "email")), dump_only=True)


# Schema instances:
one_pet = PetDetailSchema()       # to show detailed pet info (with nested user) when returning one pet
many_pets = PetSchema(many=True)    # To list pets without nested user info when returning lists of pets

# Excludes id, user_id, and is_adopted so that those fields cannot be set via /pets endpoints only /adoptions
pet_without_id = PetSchema(exclude=["id", "user_id", "is_adopted"])
