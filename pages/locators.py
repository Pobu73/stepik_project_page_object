from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON_IN_HEAD = (By.XPATH, "//a[@class='btn-default']")
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, "div.content>div#content_inner>p")
    EMPTY_BASKET = (By.CSS_SELECTOR, "div.content>div#content_inner")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    


class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, "form#login_form")
    register_form = (By.CSS_SELECTOR, "form#register_form")
    register_button = (By.XPATH, "//button[name='registration_submit']")
    input_email = (By.CSS_SELECTOR, "#id_registration-email")
    input_password = (By.CSS_SELECTOR, "#id_registration-password1")
    input_password_repeat = (By.CSS_SELECTOR, "#id_registration-password2")



class ProductPageLocators():
    button_basket = (By.CLASS_NAME, 'btn-add-to-basket')
    #product_name = (By.CSS_SELECTOR, 'div.col-sm-6 product_main>h1')
    #product_price = (By.CSS_SELECTOR, 'div.col-sm-6 product_main>p.price_color')
    product_name_in_message = (By.CSS_SELECTOR, 'div.alert.alert-safe.alert-noicon.alert-success.fade.in>div.alertinner>strong')
    product_price_in_message = (By.CSS_SELECTOR, 'div.alert.alert-safe.alert-noicon.alert-success.fade.in>div.alertinner>p:nth-child(1)>strong')
    #product_name = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    #product_price = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    #product_name = (By.CSS_SELECTOR,"#messages > div:nth-child(1) > div > strong")
    #product_price = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    product_price = (By.XPATH, "//div[@class='product_main']/p[@price_color]")
    product_name = (By.XPATH, "//div[@class='product_main']/h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div.alert.alert-safe.alert-noicon.alert-success.fade.in")
