import requests

api_url = "https://automationexercise.com/api/brandsList"


def get_request():
    response = requests.get(api_url)
    return response.json()


