import requests
from modules.logger import logger

def get_patient(api_projet1: str="http://api-projet1:8000"):
    endpoint = f"{api_projet1}/patient/"

    try:
        response = requests.get(endpoint,timeout=5)
        response.raise_for_status()
        logger.info("GET patient successful")
        return response.json()
    except Exception as e:
        logger.error("error getting patient : {e}")
        return None
    
def predict_charges(api_projet2: str = "http://api-projet2:8000", # noqa
                    age: float = None, bmi: float = None, children: int = None,
                    sexe: str = None, smoker: str = None, region: str = None):
    """
    Envoie une requête de prédiction de charges à l'API du Projet 2.
    Par défaut, utilise l'URL "http://api-projet2:8000" (service défini dans docker-compose). # noqa
    """
    endpoint = f"{api_projet2}/predict"
    payload = {
        "age": age,
        "bmi": bmi,
        "children": children,
        "sexe": sexe,
        "smoker": smoker,
        "region": region
    }
    try:
        response = requests.post(endpoint, json=payload, timeout=5)
        response.raise_for_status()
        logger.info("POST predict successful")
        data = response.json()
        return data.get("predicted_charges")
    except Exception as e:
        logger.error(f"Error predicting charges: {e}")
        return None