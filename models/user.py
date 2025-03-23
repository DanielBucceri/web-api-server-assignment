from init import db, ma
from marshmallow import fields, validate
from marshmallow.validate import Length


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    
    # this creates the relationship between the User and Pet models
    pets = db.relationship('Pet', back_populates='user') 

    # this creates the relationship between the User and Address models
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    address = db.relationship('Address', back_populates='user', uselist=False) 
    
class UserSchema(ma.Schema):
    first_name = fields.String(required=True, validate=Length(min=1))
    last_name = fields.String(required=True, validate=Length(min=1))
    email = fields.Email(required=True) 
    address_id = fields.Integer(required=False)
    phone = fields.String(required=True, validate=validate.Regexp(r'^0\d{9}$', error="Phone number must start with 0 and have 10 digits"))

    class Meta:
        fields = ("id", "first_name", "last_name", "email", "phone", "address_id")
    
    

one_user = UserSchema()
many_users = UserSchema(many=True)
user_without_id = UserSchema(exclude=["id"])