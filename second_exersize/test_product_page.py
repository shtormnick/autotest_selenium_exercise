from .pages.product_page import ProductPage
from .pages.base_page import BasePage


def test_guest_can_see_correct_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,link)
    page.open()
    page.browser.implicitly_wait(10)
    page.should_be_login_url()
    page.should_be_price()
    page.should_be_instock()
    page.should_be_write_review()
    page.should_be_add_to_cart()

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_cart()

