import unittest

from AllProductsListAPI.requests.all_products_list_requests import get_request


class TestAPIallProducts(unittest.TestCase):

    # get all the brands of the products --- de facut assert ---
    def test_get_all_brands(self):
        response = get_request()
        products = response.get("products", [])

        for product in products:
            brand = product.get("brand", "Unkown Brand")
            print(f'Brand: {brand}')