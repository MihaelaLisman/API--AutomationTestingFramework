import unittest

from AllProductsListAPI.requests.all_products_list_requests import get_request


class TestAPIallProducts(unittest.TestCase):

    # get the product with the biggest price - manually
    def test_get_biggest_price(self):
        response = get_request()
        biggest_product_id = response["products"][31]["id"]
        expected_price = "Rs. 5000"
        actual_price = response["products"][31]["price"]
        if actual_price == expected_price:
            print(f'The product with the biggest price has the id {biggest_product_id} and it costs {expected_price}')
        else:
            print(f'This product costs {actual_price}')
        assert actual_price == expected_price
