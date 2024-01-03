import unittest

from AllProductsListAPI.requests.all_products_list_requests import get_lowest_price


class TestAPIallProducts(unittest.TestCase):

    # get the product with the lowest price - manually
    def test_get_lowest_price(self):
        response = get_lowest_price()
        lowest_product_id = response["products"][10]["id"]
        expected_price = "Rs. 278"
        actual_price = response["products"][10]["price"]
        if actual_price == expected_price:
            print(f'The product with the lowest price has the id {lowest_product_id} and it costs {expected_price}')
        else:
            print(f'This product costs {actual_price}')
        assert actual_price == expected_price

