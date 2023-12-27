import requests

api_url = "https://automationexercise.com/api/brandsList"


def get_status_all_brands_list():
    response = requests.get(api_url)
    return response.json()


def get_brands_no_in_list():
    response = requests.get(api_url)
    return response.json()