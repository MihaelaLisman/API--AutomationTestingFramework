import unittest

from AllProductsListAPI.requests.all_products_list_requests import get_request


class TestAPIallProducts(unittest.TestCase):

    # get the id of the last product
    def test_get_last_product_id(self):
        response = get_request()
        expected_product_id = 43
        actual_product_id = response["products"][33]["id"]
        if actual_product_id == expected_product_id:
            print(f'The last product id is {expected_product_id}')
        else:
            print(f'The last product id is {actual_product_id}')
        assert actual_product_id == expected_product_id
