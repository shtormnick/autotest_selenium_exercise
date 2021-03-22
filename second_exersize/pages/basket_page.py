from second_exersize.pages.locators import CartPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def cart_should_be_empty(self):
        assert self.is_element_present(
            *CartPageLocators.TEXT_OF_EMPTY_CART), "Text of empty cart is absent or cart isn't emty"

    @pytest.mark.xfail
    def cart_should_not_be_empty(self):
        assert self.is_not_element_present(
            *CartPageLocators.TEXT_OF_EMPTY_CART), "Text of empty cart is absent or cart isn't emty"
