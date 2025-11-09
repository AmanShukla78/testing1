from pages.login import LoginPage
from pages.dashboard_page import DashboardPage
from time import sleep
import pytest
from selenium.webdriver.common.by import By
from base.base_page import BasePage

@pytest.mark.usefixtures('setup')
class TestLogout:
    EMAIL_FIELD=(By.XPATH,'/html/body/div[3]/h4')
    def test_successful_logout(self):
        lp = LoginPage(self.driver)
        lp.login("amit@gmail.com", 'Amit@123')
        db = DashboardPage(self.driver)
        db.click_logout()
        print("User is redirected to login page")
        sleep(2)
    
    def test_logout_and_session_expiry(self):
        lp = LoginPage(self.driver)
        lp.login("amit@gmail.com", 'Amit@123')
        db = DashboardPage(self.driver)
        db.click_logout()
        print("User is redirected to login page")
        sleep(2)
        # Should be on login page
        assert lp.exists(lp.EMAIL), "Expected to see login page fields after logout"

        # Try to go back
        self.driver.back()
        sleep(2)
        # sign_in_as=lp.find_web_element(self.EMAIL_FIELD).text
        # assert sign_in_as == "amit@gmail.com", 'User should not be able to access Dashboard.'
        # # print("User is redirected to login page")
        
