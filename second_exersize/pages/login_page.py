from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_LINK), "Login link is incorrect or abcent"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.SIGNUP_FORM), "Register form is incorrect or abcent"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "login form is incorrect or abcent"
    
    def register_new_user(self,email,password):
        registration_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        registration_email.send_keys(email)
        registration_password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        registration_password1.send_keys(password)
        registration_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        registration_password2.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTRATION)
        submit_button.click()