import unittest

from AllBrandsListAPI.requests.all_brands_list_requests import get_request


class TestAPIallBrands(unittest.TestCase):

    def test_get_status_all_brands_list(self):
        response = get_request()
        expected_response = 200
        actual_response = response["responseCode"]
        assert actual_response == expected_response, "The status is not correct."
