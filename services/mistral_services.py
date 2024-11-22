import requests

def analyse_response(user_answer, flashcard_answer):
    """
    Analyse la réponse de l'utilisateur par rapport à la réponse attendue
    en utilisant le LLM via l'API LM Studio.
    """
    prompt = (
        f"Comparer les deux réponses suivantes :\n"
        f"- Réponse attendue : {flashcard_answer}\n"
        f"- Réponse utilisateur : {user_answer}\n"
        f"Analyse les écarts entre ces réponses et donne un score de correspondance compris entre 0 et 100.\n"
        f"Le score doit refléter la similarité globale, même si des écarts mineurs (comme une erreur d'année ou de mot) sont présents.\n"
        f"Fournis une réponse au format JSON contenant deux champs :\n"
        f"{{\n"
        f"  \"correct\": pourcentage entre 0 et 100,\n"
        f"  \"explication\": \"Analyse expliquant les écarts détectés et justifiant le score donné\"\n"
        f"}}"
    )

    lm_studio_url = "http://localhost:1234/v1/completions"
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "temperature": 0.2,
        "max_tokens": 100,
    }

    try:
        response = requests.post(lm_studio_url, json=payload)
        response.raise_for_status()
        result = response.json().get("choices", [{}])[0].get("text", "")
        try:
            parsed_result = eval(result.strip())  # Décoder la réponse JSON attendue
            return parsed_result
        except (SyntaxError, ValueError):
            return {"correct": 0, "explication": "Le modèle n'a pas pu fournir une réponse structurée."}
    except requests.exceptions.RequestException as e:
        return {"correct": 0, "explication": f"Erreur de communication avec LM Studio : {str(e)}"}
