from flask import Flask
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Retrieve the API key from the environment variables
api_key = os.getenv('API_KEY')

# Import routes after Flask app is created to avoid circular imports
from routes.ia_routes import ia_routes

# Register the blueprint for IA routes
app.register_blueprint(ia_routes, url_prefix='/ia')

if __name__ == '__main__':
    app.run(debug=True)