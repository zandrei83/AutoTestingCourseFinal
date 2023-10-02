from selenium.webdriver.common.by import By
import warnings
warnings.simplefilter("ignore", ResourceWarning)


link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
   browser.get(link)
   go_to_login_page(browser)

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()