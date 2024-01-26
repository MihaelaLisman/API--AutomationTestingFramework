import unittest

from AllProductsListAPI.requests.all_products_list_requests import get_request


class TestAPIallProducts(unittest.TestCase):

    def test_get_a_product_for_kids(self):
        response = get_request()
        expected_product_usertype = "Kids"
        actual_product_usertype = response["products"][11]["category"]["usertype"]["usertype"]
        assert actual_product_usertype == expected_product_usertype, 'Usertype not matching the criteria.'
