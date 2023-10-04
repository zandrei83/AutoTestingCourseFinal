from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def input_the_answer_for_discount(self):
        BasePage.solve_quiz_and_get_code(self)

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), 'Add to Basket Button is not presented'

    def product_added_to_basket_confirmation_name(self):
        assert self.get_product_name() == self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_CONFIRMATION).text, 'Product name does not match'

    def product_added_to_basket_confirmation_price(self):
        assert self.get_product_price() == self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_CONFIRMATION).text, 'Price does not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_CONFIRMATION)

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_CONFIRMATION)
