from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(BasePage):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    SIGNUP_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    WRITE_REVIEW = (By.CSS_SELECTOR, "#write_review")
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE = (By.CLASS_NAME, "price_color")
    STOK = (By.CLASS_NAME, "instock")
    CART_PRICE = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")
    SUCCESSFULL_MESSAGE_ADD_TO_CART = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")