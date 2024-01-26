import requests

api_url = "https://automationexercise.com/api/productsList"


# get request in json format
def get_request():
    response = requests.get(api_url)
    return response.json()


# post product - method not supported
def post_product():
    response = requests.post(api_url)
    return response.json()

# # nr produse
# def get_products_no():
#     response = requests.get(api_url)
#     return response.json()
#
#
# # nume produs nr.1
# def get_first_product():
#     response = requests.get(api_url)
#     return response.json()
#
#
# # get first product usertype
# def get_a_product_for_women():
#     response = requests.get(api_url)
#     return response.json()
#
#
# def get_a_product_for_men():
#     response = requests.get(api_url)
#     return response.json()
#
#
# def get_a_product_for_kids():
#     response = requests.get(api_url)
#     return response.json()
#
#
# def get_last_product_id():
#     response = requests.get(api_url)
#     return response.json()
#
#
# def get_last_product_category():
#     response = requests.get(api_url)
#     return response.json()
#
#
# def get_lowest_price():
#     response = requests.get(api_url)
#     return response.json()
#
#
# def get_biggest_price():
#     response = requests.get(api_url)
#     return response.json()
#
#
# def get_all_brands():
#     response = requests.get(api_url)
#     return response.json()
#
#
# def get_all_men_products():
#     response = requests.get(api_url)
#     return response.json()
#
#
# def get_all_kids_products():
#     response = requests.get(api_url)
#     return response.json()
#
#
# def get_all_women_products():
#     response = requests.get(api_url)
#     return response.json()