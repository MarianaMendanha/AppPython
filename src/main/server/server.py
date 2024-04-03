# Importing necessary modules and libraries
from src.main.routes.event_routes import event_route_bp  # Importing the event_route_bp blueprint from the event_routes module
from src.main.routes.attendees_routes import  attendee_route_bp
from flask import Flask  # Importing the Flask module
from flask_cors import CORS  # Importing the CORS module for handling Cross-Origin Resource Sharing
from src.models.settings.connection import db_connection_handler  # Importing the db_connection_handler for managing database connections

# Establishing a database connection
db_connection_handler.connect_to_db()

# Initializing the Flask application
app = Flask(__name__)

# Enabling CORS for the application
CORS(app)

# Registering the event_route_bp blueprint with the Flask application
app.register_blueprint(event_route_bp)
app.register_blueprint(attendee_route_bp)