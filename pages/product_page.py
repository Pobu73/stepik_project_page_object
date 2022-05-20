from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn_basket = self.browser.find_element(*ProductPageLocators.button_basket)
        btn_basket.click()
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def should_be_right_product(self):
        product = self.browser.find_element(*ProductPageLocators.product_name).text
        prd_nm_ms = self.browser.find_element(*ProductPageLocators.product_name_in_message).text
        assert product == prd_nm_ms, 'Different products'

    def should_be_right_price(self):
        price = self.browser.find_element(*ProductPageLocators.product_price).text
        pr_nm_ms = self.browser.find_element(*ProductPageLocators.product_price_in_message).text
        assert price == pr_nm_ms, 'Different prices'
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

