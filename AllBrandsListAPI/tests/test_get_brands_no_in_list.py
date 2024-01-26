import unittest

from AllBrandsListAPI.requests.all_brands_list_requests import get_request


class TestAPIallBrands(unittest.TestCase):

    def test_get_brands_no_in_list(self):
        response = get_request()
        brands = response["brands"]
        expected_brands_no = 34
        actual_brands_no = len(brands)
        assert actual_brands_no == expected_brands_no, f"The number of brands we {expected_brands_no} does not match {actual_brands_no}."
