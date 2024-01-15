import unittest

from AllBrandsListAPI.requests.all_brands_list_requests import get_status_all_brands_list, get_brands_no_in_list


class TestAPIallBrands(unittest.TestCase):

    def test_get_status_all_brands_list(self):
        response = get_status_all_brands_list()
        expected_response = 200
        actual_response = response["responseCode"]
        assert actual_response == expected_response, "The status is not correct."
