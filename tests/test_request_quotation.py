from pages.request_quotation_page import RequestQuotationPage
from pages.login import LoginPage
from pages.dashboard_page import DashboardPage
import pytest
from time import sleep

@pytest.mark.usefixtures('setup')
class TestRequestQuotation:
    def test_request_quotation_success(self):
        lp = LoginPage(self.driver)
        lp.login("amit@gmail.com", 'Amit@123')
        
        dp = DashboardPage(self.driver)
        assert dp.is_loaded()
        dp.go_request_quotation()
        rq = RequestQuotationPage(self.driver)
        rq.fill_valid_quote("Roadside","Garage","2025","September","15")
        sleep(2)
        rq.save()
        sleep(2)
        assert rq.confirmation_present(), "Expected confirmation after saving quotation"
        print(rq.success_msg())
        assert rq.quotation_number, "Expected A confirmation/quotation number is displayed"
        print("A confirmation/quotation number is displayed")
        sleep(4)
        
    def test_request_quotation_with_missing_fields(self):
        self.driver.get("https://demo.guru99.com/insurance/v1/index.php")
        lp = LoginPage(self.driver)
        lp.login("amit@gmail.com", 'Amit@123')
        db = DashboardPage(self.driver)
        db.go_request_quotation()
        rq = RequestQuotationPage(self.driver)
        sleep(2)
        rq.save()
        sleep(2)
        assert rq.confirmation_present() and rq.quotation_number() == False, "Validation errors should shown."
        print("Validation errors are shown")
        sleep(2)
        

    def test_request_quotation_validation(self):
        self.driver.get("https://demo.guru99.com/insurance/v1/index.php")
        lp = LoginPage(self.driver)
        lp.login("amit@gmail.com", 'Amit@123')
        db = DashboardPage(self.driver)
        db.go_request_quotation()
        rq = RequestQuotationPage(self.driver)
        # Enter invalid negative value
        rq.remove_enter_text(rq.VALUE, "-100")
        sleep(2)
        rq.save()
        sleep(2)
        # Expect some validation/notice to appear
        assert rq.confirmation_present() and rq.quotation_number() == False, "Error message “Invalid data entered” should displayed"
        print("Error message “Invalid data entered” is displayed")
        
    
    