import unittest

from AllProductsListAPI.requests.all_products_list_requests import get_all_men_products


class TestAPIallProducts(unittest.TestCase):

    def test_get_all_men_products(self):
        response = get_all_men_products()
        products = response.get("products", [])
        no = 0
        expected_no = 9

        for product in products:
            usertype = product.get("category").get("usertype").get("usertype", "Unknown Category")
            if usertype == "Men":
                no += 1
                print(no)

        actual_no = no
        assert actual_no == expected_no, f"The number of articles for men should be {expected_no}, instead the actual number of items for men is {actual_no}"
