from flask import Blueprint, request, jsonify
from services.mistral_services import analyse_response

# Créer un blueprint pour les routes liées à Mistral
mistral_routes = Blueprint('mistral_routes', __name__)

@mistral_routes.route('/mistral/analyse', methods=['POST'])
def analyse_route():
    """
    Analyse la réponse de l'utilisateur par rapport à la réponse attendue.
    """
    data = request.json

    # Récupération des données utilisateur
    user_answer = data.get('userAnswer')
    flashcard_answer = data.get('flashcardAnswer')

    # Vérification des champs requis
    if not user_answer or not flashcard_answer:
        return jsonify({'error': 'Les deux réponses doivent être fournies.'}), 400

    try:
        # Appel de la fonction de service
        result = analyse_response(user_answer, flashcard_answer)
        return jsonify(result)  # Retourne directement la réponse du service
    except Exception as e:
        print("Erreur :", str(e))
        return jsonify({'error': str(e)}), 500
