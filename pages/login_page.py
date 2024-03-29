from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link is not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(str(email))
        self.browser.find_element(*LoginPageLocators.PASSWORD1).send_keys(str(password))
        self.browser.find_element(*LoginPageLocators.PASSWORD2).send_keys(str(password))
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
