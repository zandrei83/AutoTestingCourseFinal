import time

import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

import warnings
warnings.simplefilter("ignore", ResourceWarning)


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):

    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.should_be_add_to_basket_button()
    product_page.add_product_to_basket()
    product_page.input_the_answer_for_discount()

    product_page.product_added_to_basket_confirmation_name(), 'Product was NOT added to the basket, name does not match'
    product_page.product_added_to_basket_confirmation_price(), \
        'Product was NOT added to the basket, price does not match'


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/'

    product_page = ProductPage(browser, link, 0)
    product_page.open()

    product_page.should_be_add_to_basket_button()
    product_page.add_product_to_basket()

    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):

    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/'

    product_page = ProductPage(browser, link, 0)
    product_page.open()

    product_page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):

    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/'

    product_page = ProductPage(browser, link, 0)
    product_page.open()

    product_page.should_be_add_to_basket_button()
    product_page.add_product_to_basket()

    product_page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.open()
    basket_page.basket_is_empty()

class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()

        login_page.register_new_user(login_page.fake_user_email(), login_page.fake_user_password(10))
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/'

        product_page = ProductPage(browser, link, 0)
        product_page.open()

        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/'
        product_page = ProductPage(browser, link)
        product_page.open()

        product_page.should_be_add_to_basket_button()
        product_page.add_product_to_basket()

        product_page.product_added_to_basket_confirmation_name(), 'Product was NOT added to the basket, name does not match'
        product_page.product_added_to_basket_confirmation_price(), \
            'Product was NOT added to the basket, price does not match'
