from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators:
    LOG_IN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD1 = (By.ID, "id_registration-password1")
    PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocator:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div[id='messages'] > div:nth-child(1)")
    BASKET_MESSAGE_2 = (By.CSS_SELECTOR, "div[id='messages'] > div:nth-child(2)")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "div[id='messages'] > div:nth-child(1) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6 h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(3) strong")
    BASKET = (By.CSS_SELECTOR, "div.basket-mini")

class BasketPageLocator:
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "div#content_inner p")
    BASKET_PRODUCTS = (By.CSS_SELECTOR, "div#content_inner div")