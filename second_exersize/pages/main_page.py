from second_exersize.pages.locators import BasePageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def cart_should_be_empty(self):
        self.is_element_present(
            *BasePageLocators.TEXT_OF_EMPTY_CART), "Text of empty cart is absent or cart isn't emty"
