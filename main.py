from flask import Flask
from marshmallow.exceptions import ValidationError
from dotenv import load_dotenv
import os
from init import db, ma
from blueprints.db_bp import db_bp
from blueprints.addresses_bp import addresses_bp
from blueprints.adoptions_bp import adoptions_bp
# from blueprints.pets_bp import pets_bp 
# from blueprints.users_bp import users_bp


def create_app():
    app = Flask(__name__)

    load_dotenv(override=True)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')

    db.init_app(app)
    ma.init_app(app)

    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {"error": err.messages}, 400

    # Register Blueprints
    app.register_blueprint(db_bp)
    #app.register_blueprint(users_bp)
   # app.register_blueprint(pets_bp)
    app.register_blueprint(adoptions_bp)
    app.register_blueprint(addresses_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
