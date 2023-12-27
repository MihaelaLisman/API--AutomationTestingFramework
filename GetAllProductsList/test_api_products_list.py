import unittest

from GetAllProductsList.getAllProductsList import get_status, get_products_no, get_first_product, post_product, get_a_product_for_women, get_a_product_for_men, get_a_product_for_kids, get_last_product_id, get_last_product_category, get_lowest_price, get_biggest_price, get_all_brands, get_all_men_products, get_all_kids_products, get_all_women_products


class TestAPIallProducts(unittest.TestCase):

    # verificarea status
    def test_get_status(self):
        response = get_status()
        status = response['responseCode']
        assert status == 200, 'Invalid API Status'

    # verificare nr produse
    def test_get_products_no(self):
        response = get_products_no()
        products = response["products"]
        expected_products_no = 34
        actual_products_no = len(products)
        assert actual_products_no == expected_products_no, f'The number of products is not correct. We were expecting {expected_products_no}, but got {actual_products_no}'

    # verificare nume produs nr. 1
    def test_get_first_product(self):
        response = get_first_product()
        expected_product_name = "Blue Top"
        actual_product_name = response["products"][0]["name"]
        if actual_product_name == expected_product_name:
            print(f'The product {actual_product_name} is on stock.')
        else:
            print(f'Product not found, product needed: {expected_product_name}, product found: {actual_product_name}.')
        assert actual_product_name == expected_product_name

    # post new product - This request method is not supported.
    def test_post_new_product(self):
        response = post_product()
        response_status = response["responseCode"]
        assert response_status == 405

    # get all products that are for the females
    def test_get_a_product_for_women(self):
        response = get_a_product_for_women()
        expected_product_usertype = "Women"
        actual_product_usertype = response["products"][0]["category"]["usertype"]["usertype"]
        assert actual_product_usertype == expected_product_usertype, 'Usertype not matching the criteria.'
        # print(response["products"])

    def test_get_a_product_for_men(self):
        response = get_a_product_for_men()
        expected_product_usertype = "Men"
        actual_product_usertype = response["products"][21]["category"]["usertype"]["usertype"]
        assert actual_product_usertype == expected_product_usertype, 'Usertype not matching the criteria.'

    def test_get_a_product_for_kids(self):
        response = get_a_product_for_kids()
        expected_product_usertype = "Kids"
        actual_product_usertype = response["products"][11]["category"]["usertype"]["usertype"]
        assert actual_product_usertype == expected_product_usertype, 'Usertype not matching the criteria.'

    # get the id of the last product
    def test_get_last_product_id(self):
        response = get_last_product_id()
        expected_product_id = 43
        actual_product_id = response["products"][33]["id"]
        if actual_product_id == expected_product_id:
            print(f'The last product id is {expected_product_id}')
        else:
            print(f'The last product id is {actual_product_id}')
        assert actual_product_id == expected_product_id

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

    # get the product with the biggest price - manually
    def test_get_biggest_price(self):
        response = get_biggest_price()
        biggest_product_id = response["products"][31]["id"]
        expected_price = "Rs. 5000"
        actual_price = response["products"][31]["price"]
        if actual_price == expected_price:
            print(f'The product with the biggest price has the id {biggest_product_id} and it costs {expected_price}')
        else:
            print(f'This product costs {actual_price}')
        assert actual_price == expected_price

    # get all the brands of the products --- de facut assert ---
    def test_get_all_brands(self):
        response = get_all_brands()
        products = response.get("products", [])

        for product in products:
            brand = product.get("brand", "Unkown Brand")
            print(f'Brand: {brand}')

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

    def test_get_all_women_products(self):
        response = get_all_women_products()
        products = response.get("products", [])
        no = 0
        expected_no = 12

        for product in products:
            usertype = product.get("category").get("usertype").get("usertype", "Unknown Category")
            if usertype == "Women":
                no += 1
                print(no)

        actual_no = no
        assert actual_no == expected_no, f"The number of articles for women should be {expected_no}, instead the actual number of items for women is {actual_no}"

    def test_get_all_kids_products(self):
        response = get_all_kids_products()
        products = response.get("products", [])
        no = 0
        expected_no = 13

        for product in products:
            usertype = product.get("category").get("usertype").get("usertype", "Unknown Category")
            if usertype == "Kids":
                no += 1
                print(no)

        actual_no = no
        assert actual_no == expected_no, f"The number of articles for kids should be {expected_no}, instead the actual number of items for kids is {actual_no}"
