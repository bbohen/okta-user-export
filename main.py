import os
import requests
from dotenv import load_dotenv

from create_csv import create_csv

DOTENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(DOTENV_PATH)


def init():
    api_token = os.getenv('API_TOKEN')
    okta_root_url = os.getenv('OKTA_ROOT_URL')
    group_id = os.getenv('GROUP_ID')
    okta_headers = {
        'Authorization': 'SSWS ' + api_token
    }
    url = '{}/api/v1/groups/{}/users'.format(okta_root_url, group_id)
    response = requests.get(url, headers=okta_headers)
    response_data = response.json()

    create_csv(response_data)


init()
