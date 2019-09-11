from .base_page import BasePage
from .locators import ProductPageLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocator.ADD_TO_BASKET_BUTTON).click()

    def should_not_be_success_messages(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='messages'] > div:nth-child(1)")))
        assert self.is_element_present(*ProductPageLocator.SUCCESS_MESSAGE), "First message is not present"
        assert self.is_element_present(*ProductPageLocator.BASKET_MESSAGE_2), "Second message is not present"

    def should_be_equal_names(self):
        message = self.browser.find_element(*ProductPageLocator.SUCCESS_MESSAGE_PRODUCT_NAME).text
        product_name = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME).text
        assert message == product_name, f"Product names is not equal,{message},{product_name}"

    def should_be_equal_amounts(self):
        amount = self.browser.find_element(*ProductPageLocator.BASKET).text.split()[2]
        price = self.browser.find_element(*ProductPageLocator.PRODUCT_PRICE).text
        assert amount == price, f"Basket sum and product price are not equal,{amount},{price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocator.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocator.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
