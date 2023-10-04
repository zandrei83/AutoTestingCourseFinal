from .base_page import BasePage
from .locators import BasketPageLocators

import warnings
warnings.simplefilter("ignore", ResourceWarning)

class BasketPage(BasePage):

    def basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT)

    def no_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_LIST)
