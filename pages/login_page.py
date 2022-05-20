from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url(), 'current url not corrected'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            By.CSS_SELECTOR, "form#login_form"), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            By.CSS_SELECTOR, "form#register_form"), "Register form is not presented"
    
    def register_new_user(self, email, password):
        input_email = self.is_element_present(*LoginPageLocators.input_email)
        input_email.send_keys(email)
        input_passwd = self.is_element_present(*LoginPageLocators.input_password)
        input_passwd.send_keys(password)
        input_passw_repeat = self.is_element_present(*LoginPageLocators.input_password_repeat)
        input_passw_repeat.send_keys(password)
        register_btn = self.is_element_present(*LoginPageLocators.register_button)
        register_btn.click()
