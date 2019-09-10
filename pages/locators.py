from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOG_IN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocator:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME,"btn-add-to-basket")
    BASKET_MESSAGE_1 = (By.CSS_SELECTOR, "div[id='messages'] > div:nth-child(1)")
    BASKET_MESSAGE_2 = (By.CSS_SELECTOR, "div[id='messages'] > div:nth-child(2)")
    BASKET_MESSAGE_1_PRODUCT_NAME = (By.CSS_SELECTOR,"div[id='messages'] > div:nth-child(1) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6 h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(3) strong")
    BASKET = (By.CSS_SELECTOR, "div.basket-mini")