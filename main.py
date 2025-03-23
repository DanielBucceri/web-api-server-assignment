from flask import Flask
from marshmallow import ValidationError
from dotenv import load_dotenv
import os
from init import db, ma
from blueprints.db_bp import db_bp
from blueprints.addresses_bp import addresses_bp
from blueprints.adoptions_bp import adoptions_bp
from blueprints.pets_bp import pets_bp 
from blueprints.users_bp import users_bp   
from flask import jsonify


def create_app():
    """
    Flask app factory pattern for creating and configuring the application instance.
    """
    app = Flask(__name__)

    # Load environment variables from .env file
    load_dotenv(override=True)

    # Configure the database URI using environment variable
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')

    # Initialize SQLAlchemy and Marshmallow with the app context
    db.init_app(app)
    ma.init_app(app)

    # Handle validation errors raised by Marshmallow schemas globally
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {"error": err.messages}, 400

    # Register all application blueprints (modular route groupings)
    app.register_blueprint(db_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(pets_bp)
    app.register_blueprint(adoptions_bp)
    app.register_blueprint(addresses_bp)

    # Global error handlers for common HTTP errors
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({"error": "Bad request"}), 400

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Internal server error"}), 500

    return app
    

# Run the Flask development server if this script is executed directly
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


app = create_app()
