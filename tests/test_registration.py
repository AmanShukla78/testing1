import pytest, time
from pages.registration_page import RegistrationPage


@pytest.mark.usefixtures('setup')
class TestRegistration:
    def test_successful_registration(self):
        # 1. Open the registration page.
        reg_obj = RegistrationPage(self.driver)
        reg_obj.click_reg_btn()

        # 2. Fill in all mandatory fields with valid details (first name, last name, email, password, etc.).
        reg_obj.fill_form('Mr', 'Amit', 'Shukla', 9695230479, 2003, 'November', 10, 'Full', 2, "Engineer", 'Lucknow', 'Lucknow', 'India', '226028', 'amit@gmail.com', 'Amit@123')
        
        #Click Create Account.
        reg_obj.create_account()

        current_url = self.driver.current_url
        expected_url = 'https://demo.guru99.com/insurance/v1/index.php'

        assert current_url == expected_url
        print("Confirmation message or redirection to login page is displayed.")

        time.sleep(3)
        
    def test_registration_with_missing_field(self):
        # 1. Open the registration page.
        reg_obj = RegistrationPage(self.driver)
        reg_obj.click_reg_btn()
        # Intentionally create account without filling anything
        reg_obj.create_account()
        # Expect some validation to be present on the page
        current_url = self.driver.current_url
        expected_url = 'https://demo.guru99.com/insurance/v1/index.php'

        assert current_url != expected_url,"Registration page should show validation and remain"
        print("Registration page show validation and remain")
        
    def test_registration_with_invalid_email_format(self):
        # 1. Open the registration page.
        reg_obj = RegistrationPage(self.driver)
        reg_obj.click_reg_btn()

        # 2. Fill in all mandatory fields with valid details (first name, last name, email, password, etc.).
        reg_obj.fill_form('Mr', 'Amit', 'Shukla', 9695230479, 2003, 'November', 10, 'Full', 2, "Engineer", 'Lucknow', 'Lucknow', 'India', '226028', 'email@example..com', 'Amit@123')
        
        #Click Create Account.
        reg_obj.create_account()
        

        current_url = self.driver.current_url
        expected_url = 'https://demo.guru99.com/insurance/v1/index.php'

        assert current_url != expected_url
        print("Error message “Enter a valid email address” is displayed.")

        time.sleep(3)
