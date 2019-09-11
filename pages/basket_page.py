from .base_page import BasePage
from .locators import BasketPageLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasketPage(BasePage):

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocator.BASKET_PRODUCTS), "Products in the basket but should not be"

    def should_be_text(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocator.BASKET_IS_EMPTY_TEXT).text
        assert "empty" in empty_basket_text, "Text that the basket is empty is missing"