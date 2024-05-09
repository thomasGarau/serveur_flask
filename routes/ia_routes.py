from flask import Blueprint, request, jsonify
from services.ia_service import predict
from services.auth import require_api_key

ia_routes = Blueprint('ia_routes', __name__)

@ia_routes.route('/predict', methods=['POST'])
@require_api_key
def prediction():
    data = request.get_json()
    result = predict(data)
    return jsonify(result)
