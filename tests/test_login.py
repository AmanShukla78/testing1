import pytest
from pages.login import LoginPage
from pages.dashboard_page import DashboardPage
from time import sleep

@pytest.mark.usefixtures('setup')
class TestLogin:
    def test_login_success(self):
        lp = LoginPage(self.driver)
        lp.login("amit@gmail.com", 'Amit@123')
        current_url = self.driver.current_url
        assert current_url == "https://demo.guru99.com/insurance/v1/header.php"
        print("User is redirected to Dashboard page")


    def test_login_invalid_credentials(self):
        self.driver.get("https://demo.guru99.com/insurance/v1/index.php")
        lp = LoginPage(self.driver)
        lp.login("amit1@gmail.com", 'aby')
        sleep(2)
        error_msg=lp.error_message_present()
        assert error_msg == "Enter your Email address and password correct"
        print("Enter your Email address and password correct - appears")
        print("User remains on login page.")

    def test_login_empty_credentials(self):
        lp = LoginPage(self.driver)
        lp = LoginPage(self.driver)
        lp.login("","" )
        # current_url = self.driver.current_url
        # assert current_url != "https://demo.guru99.com/insurance/v1/header.php", 'Expected error message for empty login.'
        assert lp.error_message_present(), "Expected error message for empty login is not displayed"
        print("Expected error message for empty login")
        
