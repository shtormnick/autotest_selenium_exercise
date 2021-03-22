from .pages.basket_page import BasketPage
import pytest


def test_guest_can_see_product_in_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/basket/"
    page = BasketPage(browser, link)
    page.open()
    page.cart_should_not_be_empty()


def test_guest_cant_see_product_in_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/basket/"
    page = BasketPage(browser, link)
    page.open()
    page.cart_should_be_empty()
