from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.XPATH, "//span[@class='btn-group']/a[@class='btn btn-default']")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL_TEXT = 'login'
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p')
    PRODUCT_NAME_CONFIRMATION = (By.XPATH, '//div[@class="alertinner "]/strong')
    PRODUCT_PRICE_CONFIRMATION = (By.XPATH, '//div[@class="alertinner "]/p/strong')


class BasketPageLocators:
    BASKET_EMPTY_TEXT = (By.XPATH, '//div[@id="content_inner"]/p/a')
    BASKET_ITEMS_LIST = (By.CLASS_NAME, 'basket-items')
