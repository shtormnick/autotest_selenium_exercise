from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_price()
        self.should_be_instock()
        self.should_be_add_to_cart()
        self.should_be_write_review()
        self.add_to_cart()
        self.should_not_be_success_message()
        self.should_dissapeared_success_message()

    def should_be_price(self):
        assert self.is_element_present(
            *ProductPageLocators.PRICE), "Prise is abcent"

    def should_be_instock(self):
        assert self.is_element_present(
            *ProductPageLocators.STOK), "Stok is abcent"

    def should_be_add_to_cart(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_CART), "Add to Cart is abcent"

    def should_be_write_review(self):
        assert self.is_element_present(
            *ProductPageLocators.WRITE_REVIEW), "Write review button is abcent"

    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        button.click()
        self.solve_quiz_and_get_code()
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        cart_price = self.browser.find_element(
            *ProductPageLocators.CART_PRICE).text
        alert_message = self.browser.find_element(
            *ProductPageLocators.SUCCESSFULL_MESSAGE_ADD_TO_CART).text
        book_title = self.browser.find_element(
            *ProductPageLocators.BOOK_TITLE).text
        assert price == cart_price, "price and cart price is not match"
        assert alert_message == book_title, "added book is not math"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSFULL_MESSAGE_ADD_TO_CART), \
            "Success message is present, but shouldn't"
    
    def should_dissapeared_success_message(self):
        assert self.is_dissapeared(*ProductPageLocators.SUCCESSFULL_MESSAGE_ADD_TO_CART), \
            "Success message is not dissapeared, but should"
    