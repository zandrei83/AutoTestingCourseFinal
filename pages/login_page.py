from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert False if self.browser.current_url.find(
            LoginPageLocators.LOGIN_URL_TEXT) == -1 else True, 'There is no "{}" in {}'.format(
            LoginPageLocators.LOGIN_URL_TEXT, self.browser.current_url)

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Element not found on the page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Element not found on the page'

    def register_new_user(self, email, password):

        self.browser.find_element(*LoginPageLocators.REGISTER_USER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_USER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_USER_PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_USER_SUBMIT_BUTTON).click()



