import unittest

from AllProductsListAPI.requests.all_products_list_requests import get_request


class TestAPIallProducts(unittest.TestCase):

    # verificare nr produse
    def test_get_products_no(self):
        response = get_request()
        products = response["products"]
        expected_products_no = 34
        actual_products_no = len(products)
        assert actual_products_no == expected_products_no, f'The number of products is not correct. We were expecting {expected_products_no}, but got {actual_products_no}'
