import requests
import logging

# Logging format
LOGGING_FORMAT = '%(asctime)s %(process)d %(name)s %(levelname)s: %(message)s'

logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "https://api.embeddify.io/v1"
# Configuration variable to store the API key
global api_key


def show_debug():
    return True


def post_data(endpoint, data):
    global api_key
    if api_key is None:
        raise Exception("API key is not configured. Call configure(api_key) first.")

    url = f"{BASE_URL}/{endpoint}"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    logger.info(f"/POST to {url} {data}")
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201 or response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code} \n {response.json()}")


def get_data(endpoint):
    global api_key
    if api_key is None:
        raise Exception("API key is not configured. Call configure(api_key) first.")

    url = f"{BASE_URL}/{endpoint}"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code} \n {response.json()}")
