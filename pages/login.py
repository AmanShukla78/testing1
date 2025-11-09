from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.NAME, "submit")
    ERROR = (By.XPATH, '//*[@id="login-form"]/div[2]/span/b')

    def login(self, email, password):
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.click_operation(self.LOGIN_BTN)

    def error_message_present(self):
        return self.find_web_element(self.ERROR).text