import pytest
from pages.login import LoginPage
from pages.dashboard_page import DashboardPage
from time import sleep

@pytest.mark.usefixtures('setup')
class TestDashboard:
    def test_dashboard_links_visible(self):
        lp = LoginPage(self.driver)
        lp.login("amit@gmail.com", 'Amit@123')
        
        dp = DashboardPage(self.driver)
        assert dp.is_loaded()
        
        # Verify nav links presence (visibility is checked on click attempt)
        assert dp.exists(dp.LINK_REQUEST_QUOTE)
        assert dp.exists(dp.LINK_RETRIEVE_QUOTE)
        assert dp.exists(dp.LINK_PROFILE)
        # assert dp.exists(dp.LINK_LOGOUT)
        print("Dashboard page loads with links to Request Quotation, Retrieve Quotation, Profile")
        
    def test_verify_navigation_links(self):
        dp = DashboardPage(self.driver)
        assert dp.is_loaded()
        sleep(2)
        
        # From Dashboard, click on each navigation link
        dp.go_request_quotation()
        assert dp.exists(dp.IS_NAVIGATE_REQUEST)
        print("Request quote page is loaded")
        sleep(2)
        
        dp.go_retrieve_quotation()
        assert dp.exists(dp.IS_NAVIGATE_RETRIEVE)
        print("Retrieve quote page is loaded")
        sleep(2)
        
        dp.go_profile()
        assert dp.exists(dp.IS_NAVIGATE_PROFILE)
        print("Profile page is loaded")
        sleep(2)
        
        dp.go_edit()
        assert dp.exists(dp.IS_NAVIGATE_EDIT)
        print("Edit page is loaded")
        sleep(2)
        
        dp.go_home()
        assert dp.exists(dp.IS_NAVIGATE_EDIT)
        print("Home page is loaded")
        sleep(2)
        
        
        print("Correct respective page is loaded.")
        
        
        
        
        