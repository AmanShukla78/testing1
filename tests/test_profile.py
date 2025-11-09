import pytest, time
from pages.profile_page import  Profile
from config.config import Config
from util.browser_factory import get_browser
from pages.login import LoginPage

@pytest.mark.usefixtures('setup')
class Test15:
    def test_update_profile_with_valid_data(self):
        lp = LoginPage(self.driver)
        lp.login("amit@gmail.com", 'Amit@123')
        
        profile = Profile(self.driver)
        profile.click_profile()

        profile.user_details('Mrs', 'Nidhi', 'Saha', 2345644, 2006, 'November', 1, 2, "Engineer", 'Kanpur', 'Kanpur', 'India', '206251')
        profile.submit()
        
    def test_update_profile_with_missing_field(self):
        self.driver.get("https://demo.guru99.com/insurance/v1/index.php")
        lp = LoginPage(self.driver)
        lp.login("amit@gmail.com", 'Amit@123')
        
        profile = Profile(self.driver)
        profile.click_profile()

        profile.user_details('Mrs', '', '', 2345644, 2006, '', 1, 2, "", '', '', '', '')
        profile.submit()