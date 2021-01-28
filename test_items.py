import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_button_add_to_basket_should_exist(browser):
    browser.get(link)
    add_to_cart_button = browser.find_element_by_class_name(
        "btn-add-to-basket")
    try:
        assert add_to_cart_button is not None
    except:
        print("Something wrong with this fuking button")
