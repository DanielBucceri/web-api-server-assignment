from init import db, ma
from sqlalchemy.orm import relationship
from marshmallow import fields
from datetime import datetime

class Adoption(db.Model):
    __tablename__ = 'adoptions'
    
    id = db.Column(db.Integer, primary_key=True)
    adoption_date = db.Column(db.DateTime, default=datetime, nullable=False) # set adoption_date to current when record is created
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))
    notes = db.Column(db.String(255))
    

class AdoptionSchema(ma.Schema):
    adoption_date = fields.DateTime(dump_only=True) # dump_only for read only
    user_id = fields.Integer(required=True)
    pet_id = fields.Integer(required=True)
    notes = fields.String(required=False)
    
    class Meta:
        fields = ("id", "adoption_date", "user_id", "pet_id", "notes")  
        
one_adoption = AdoptionSchema()
many_adoptions = AdoptionSchema(many=True)
adoption_without_id = AdoptionSchema(exclude=["id"])
        
      
