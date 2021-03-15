from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    SIGNUP_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    WRITE_REVIEW = (By.CSS_SELECTOR, "#write_review")
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    STOK = (By.CLASS_NAME, "instock")
    CART_PRICE = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")
    SUCCESSFULL_MESSAGE_ADD_TO_CART = (
        By.CSS_SELECTOR, "#messages>div:nth-child(1) .alertinner strong")
    BOOK_TITLE = (By.TAG_NAME, "h1")
