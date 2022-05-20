from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_text_empty_basket(self):
        assert self.is_element_present(
            *BasePageLocators.TEXT_EMPTY_BASKET).text, "Basket is not empty"

    def should_be_not_product_in_basket(self):
       assert self.is_element_present(
           *BasePageLocators.EMPTY_BASKET), "Products has in basket"
    
    def should_not_be_text_empty_basket(self):
        assert self.is_not_element_present(
            *BasePageLocators.TEXT_EMPTY_BASKET).text, "Empty basket text is presented, but should not be"



