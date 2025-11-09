from pages.retrive_quotation_page import RetrieveQuotationPage
from pages.login import LoginPage
from pages.dashboard_page import DashboardPage
from time import sleep
import pytest

@pytest.mark.usefixtures('setup')
class TestRetrieveQuotation:
    def test_retrieve_quotation_valid_id(self):
        lp = LoginPage(self.driver)
        lp.login("amit@gmail.com", 'Amit@123')
        DashboardPage(self.driver).go_retrieve_quotation()
        rq = RetrieveQuotationPage(self.driver)
        rq.retrieve("49565")
        assert rq.result_present(), "Expected message/result area to appear for invalid ID"
        print("Quotation details are displayed.")
        sleep(2)
        
    def test_retrieve_quotation_invalid_id(self):
        self.driver.back()
        DashboardPage(self.driver).go_retrieve_quotation()
        rq = RetrieveQuotationPage(self.driver)
        rq.retrieve("4599988877")
        msg=rq.get_error_msg()
        assert msg == "Wrong Retrieve Quotation ID. Please Check..."
        print("Error message “No quotation found” is displayed")
        sleep(2)
        
    def test_retrieve_quotation_empyt_field(self):
        self.driver.back()
        DashboardPage(self.driver).go_retrieve_quotation()
        rq = RetrieveQuotationPage(self.driver)
        rq.retrieve("")
        url=self.driver.current_url
        print(url)
        assert url != "https://demo.guru99.com/insurance/v1/retrieve_quotation.php"
        print("Error “Quotation ID is required” is displayed")
        sleep(2)
