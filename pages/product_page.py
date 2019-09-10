from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocator.ADD_TO_BASKET_BUTTON).click()

    def can_guest_see_confirmation_messages(self):
        assert self.is_element_present(*ProductPageLocator.BASKET_MESSAGE_1),"First message is not present"
        assert self.is_element_present(*ProductPageLocator.BASKET_MESSAGE_2), "Second message is not present"
        message = self.browser.find_element(*ProductPageLocator.BASKET_MESSAGE_1_PRODUCT_NAME).text
        product_name = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME).text
        assert message == product_name, f"Product names is not equal,{message},{product_name}"
        sum = self.browser.find_element(*ProductPageLocator.BASKET).text.split()[2]
        price = self.browser.find_element(*ProductPageLocator.PRODUCT_PRICE).text
        assert sum == price, f"Basket sum and product price are not equal,{sum},{price}"