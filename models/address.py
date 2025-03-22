from init import db, ma
from marshmallow import fields, validate


class Address(db.Model):
    __tablename__ = 'addresses'
    
    # creating the columns for the addresses table
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(100), nullable=False)
    suburb = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)
    
    user = db.relationship('User', back_populates='address', uselist=False)
    
class AddressSchema(ma.Schema):
    street = fields.String(required=True, validate=validate.Length(min=1, max=150))
    suburb = fields.String(required=False, validate=validate.Length(max=100))
    city = fields.String(required=True, validate=validate.Length(min=1, max=100, error="City must be 100 characters or less"))
    state = fields.String(required=True, validate=validate.Length(min=1, max=50, error="State must be 50 characters or less"))
    postcode = fields.String(required=True, validate=validate.Length(min=1, max=10, error="Postcode must be 10 characters or less"))
    country = fields.String(required=True, validate=validate.Length(min=1, max=50, error="Country must be 50 characters or less")) 
    
    class Meta:
        fields = ("id", "street", "suburb", "city", "state", "postcode", "country")
    
one_address = AddressSchema()
many_addresses = AddressSchema(many=True)
# the one_address instance is for a single address
# the many_addresses instance returns list of addresses
address_without_id = AddressSchema(exclude=['id']) # this line is creating a schema instance that excludes the id field for validation so users cannot specify the primary key


    
    
    