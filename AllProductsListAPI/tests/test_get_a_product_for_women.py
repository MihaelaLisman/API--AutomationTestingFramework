import unittest

from AllProductsListAPI.requests.all_products_list_requests import get_a_product_for_women


class TestAPIallProducts(unittest.TestCase):

    # get a product that is for a woman
    def test_get_a_product_for_women(self):
        response = get_a_product_for_women()
        expected_product_usertype = "Women"
        actual_product_usertype = response["products"][0]["category"]["usertype"]["usertype"]
        assert actual_product_usertype == expected_product_usertype, 'Usertype not matching the criteria.'
        # print(response["products"])
