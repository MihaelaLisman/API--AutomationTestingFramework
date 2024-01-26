import unittest

from AllProductsListAPI.requests.all_products_list_requests import get_request


class TestAPIallProducts(unittest.TestCase):

    # verificare status
    def test_get_status(self):
        response = get_request()
        status = response['responseCode']
        assert status == 200, 'Invalid API Status'

