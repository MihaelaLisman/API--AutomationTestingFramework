import unittest

from GetAllBrandsList.getAllBrandsList import get_status_all_brands_list, get_brands_no_in_list


class TestAPIallBrands(unittest.TestCase):

    def test_get_status_all_brands_list(self):
        response = get_status_all_brands_list()
        expected_response = 200
        actual_response = response["responseCode"]
        assert actual_response == expected_response, "The status is not correct."

    def test_get_brands_no_in_list(self):
        response = get_brands_no_in_list()
        brands= response["brands"]
        expected_brands_no = 34
        actual_brands_no = len(brands)
        assert actual_brands_no == expected_brands_no, f"The number of brands we {expected_brands_no} does not match {actual_brands_no}."
