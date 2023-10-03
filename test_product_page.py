from .pages.product_page import ProductPage

import warnings
warnings.simplefilter("ignore", ResourceWarning)


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.should_be_add_to_basket_button()
    product_page.add_product_to_basket()
    product_page.input_the_answer_for_discount()

    product_page.product_added_to_basket_confirmation_name(), 'Product was NOT added to the basket, name does not match'
    product_page.product_added_to_basket_confirmation_price(), 'Product was NOT added to the basket, price does not match'
