import unittest

from AllProductsListAPI.requests.all_products_list_requests import post_product


class TestAPIallProducts(unittest.TestCase):

    # post new product - This request method is not supported.
    def test_post_new_product(self):
        response = post_product()
        response_status = response["responseCode"]
        assert response_status == 405
