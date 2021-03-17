from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_url()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open()
    page.should_be_login_link()

def test_guest_can_see_correct_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
    page = LoginPage(browser,link)
    page.open()
    page.should_be_login_url()
    page.should_be_register_form()
    page.should_be_login_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open()
    page.go_to_cart_page()
    page.cart_should_be_empty()