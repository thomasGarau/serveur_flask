from functools import wraps
from flask import request, jsonify
import os

# Ensure that dotenv is loaded if this service might be used standalone in some contexts
from dotenv import load_dotenv
load_dotenv()

# Retrieve the API key from environment variables
API_KEY = os.getenv('API_KEY')

def require_api_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        # Checking the provided API key against the one in the environment
        if request.headers.get('x-api-key') != API_KEY:
            return jsonify({"error": "Unauthorized access"}), 403
        return view_function(*args, **kwargs)
    return decorated_function
