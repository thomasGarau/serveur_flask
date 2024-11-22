from flask import Flask
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Retrieve the API key from the environment variables
api_key = os.getenv('API_KEY')

from routes.ia_routes import ia_routes
from routes.mistral_routes import mistral_routes


app.register_blueprint(ia_routes, url_prefix='/ia')
app.register_blueprint(mistral_routes)

if __name__ == '__main__':
    app.run(debug=True)