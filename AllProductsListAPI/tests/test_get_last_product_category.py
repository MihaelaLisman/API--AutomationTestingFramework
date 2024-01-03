import unittest

from AllProductsListAPI.requests.all_products_list_requests import get_last_product_category


class TestAPIallProducts(unittest.TestCase):

    # get the category of the last product
    def test_get_last_product_category(self):
        response = get_last_product_category()
        expected_product_category = "Tshirts"
        actual_product_category = response["products"][33]["category"]["category"]
        if actual_product_category == expected_product_category:
            print(f'The last product is from category: {expected_product_category}')
        else:
            print(f'The last product is from category: {actual_product_category}')
        assert actual_product_category == expected_product_category

