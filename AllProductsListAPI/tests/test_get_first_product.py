import unittest

from AllProductsListAPI.requests.all_products_list_requests import get_first_product


class TestAPIallProducts(unittest.TestCase):

    # verificare nume produs nr. 1
    def test_get_first_product(self):
        response = get_first_product()
        expected_product_name = "Blue Top"
        actual_product_name = response["products"][0]["name"]
        if actual_product_name == expected_product_name:
            print(f'The product {actual_product_name} is on stock.')
        else:
            print(f'Product not found, product needed: {expected_product_name}, product found: {actual_product_name}.')
        assert actual_product_name == expected_product_name

