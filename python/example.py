"""
The purpose of this code is to show how to work with plant.id API.
You'll find API documentation at https://plant.id/api
"""

import base64
import requests
from time import sleep


secret_access_key = "-- ask for one at business@plant.id --"


class SendForIdentificationError(Exception):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


def encode_files(file_names):
    files_encoded = []
    for file_name in file_names:
        with open(file_name, "rb") as file:
            files_encoded.append(base64.b64encode(file.read()).decode("ascii"))
    return files_encoded


def identify_plant(file_names):
    images = encode_files(file_names)

    # see the docs for more optional attributes
    params = {
        "api_key": secret_access_key,
        "images": images,
        "modifiers": ["crops_fast", "similar_images"],
        "plant_language": "en",
        "plant_details": ["common_names", "url", "name_authority", "wiki_description", "taxonomy"],
        }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post("https://api.plant.id/v2/identify",
                             json=params,
                             headers=headers)

    if response.status_code != 200:
        raise SendForIdentificationError(response.text)

    return response.json()


if __name__ == '__main__':
    print(identify_plant(["photo1.jpg", "photo2.jpg"]))
