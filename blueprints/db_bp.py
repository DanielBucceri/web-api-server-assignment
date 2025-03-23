from flask import Blueprint
from init import db
from datetime import date
from models.user import User
from models.address import Address
from models.pet import Pet
from models.adoption import Adoption


db_bp = Blueprint('db', __name__)

@db_bp.cli.command('init')
def init_db():
    db.drop_all()
    db.create_all()
    print("Database tables dropped and recreated.")

@db_bp.cli.command('seed')
def seed_db():
    # Addresses
    addr1 = Address(
        street="123 Main St",
        suburb="CBD",
        city="Sydney",
        country="Australia",
        state="NSW",
        postcode="2000"
    )

    addr2 = Address(
        street="78 Sunset Blvd",
        suburb="Westside",
        city="Brisbane",
        country="Australia",
        state="QLD",
        postcode="4000"
    )

    # Users
    u1 = User(first_name="Alice", last_name="Smith", email="alice@example.com", phone="0400000001", address=addr1)
    u2 = User(first_name="Bob", last_name="Jones", email="bob@example.com", phone="0400000002", address=addr2)

    # Pets (using the updated boolean field is_adopted)
    p1 = Pet(
        name="Buddy",
        species="Dog",
        age=3,
        color="Brown",
        is_adopted=False  # Pet is available no owner assigned yet
    )

    p2 = Pet(
        name="Mittens",
        species="Cat",
        age=2,
        color="Black and White",
        is_adopted=False  # Pet is available
    )

    db.session.add_all([u1, u2, p1, p2])
    db.session.commit()

    # Simulate an adoption event:
    # User u2 adopts pet p1.
    adopt = Adoption(user_id=u2.id, pet_id=p1.id, notes="Rescued from local shelter")
    db.session.add(adopt)
    db.session.commit()

    # Update pet p1 to reflect that it is now adopted.
    p1.user_id = u2.id
    p1.is_adopted = True
    db.session.commit()

    print("Database seeded with sample data!")


    # Adoptions record
    adopt = Adoption(user_id=u2.id, pet_id=p1.id, notes="Rescued from local shelter")
    db.session.add(adopt)
    db.session.commit()

    print("Database seeded with sample data!")
