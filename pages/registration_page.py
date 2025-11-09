from base.base_page import BasePage
from util.scroll_util import ScrollUtil
from selenium.webdriver.common.by import By

class RegistrationPage(BasePage):
    REGISTRATIN_BTN = (By.XPATH, '/html/body/div[3]/a')
    TITLE_FIELD = (By.XPATH, '//*[@id="user_title"]')
    FIRST_NAME_FIELD = (By.XPATH, '//*[@id="user_firstname"]')
    LAST_NAME_FIELD = (By.XPATH, '//*[@id="user_surname"]')
    PHONE_FIELD = (By.XPATH, '//*[@id="user_phone"]')
    YEAR_FIELD = (By.XPATH, '//*[@id="user_dateofbirth_1i"]')
    MONTH_FIELD = (By.XPATH, '//*[@id="user_dateofbirth_2i"]')
    DAY_FIELD = (By.XPATH, '//*[@id="user_dateofbirth_3i"]')
    FULL_TYPE = (By.XPATH, '//*[@id="licencetype_t"]')
    PROVISIONAL_TYPE = (By.XPATH, '//*[@id="licencetype_f"]')

    LICENCE_PERIOD = (By.XPATH, '//*[@id="user_licenceperiod"]')
    OCCUPATION = (By.XPATH, '//*[@id="user_occupation_id"]')
    STREET = (By.XPATH, '//*[@id="user_address_attributes_street"]')
    CITY = (By.XPATH, '//*[@id="user_address_attributes_city"]')
    COUNTRY = (By.XPATH, '//*[@id="user_address_attributes_county"]')
    PIN_CODE = (By.XPATH, '//*[@id="user_address_attributes_postcode"]')
    EMAIL = (By.XPATH, '//*[@id="user_user_detail_attributes_email"]')
    PASSWORD = (By.XPATH, '//*[@id="user_user_detail_attributes_password"]')
    REPASSWORD = (By.XPATH, '//*[@id="user_user_detail_attributes_password_confirmation"]')
    CREATE = (By.XPATH, '//*[@id="new_user"]/div[5]/input[2]')
    RESET = (By.XPATH, '//*[@id="resetform"]')
    


    def click_reg_btn(self):
        self.click_operation(self.REGISTRATIN_BTN)
    
    def fill_form(self, title, fname, lname, phone, year, month, day, type, licence_period, occupatation, street, city, country, pin, email, password):
        scroll_obj = ScrollUtil(self.driver)
        scroll_obj.scroll_by(0, 170)
        self.enter_text(self.TITLE_FIELD, title)
        self.enter_text(self.FIRST_NAME_FIELD, fname)
        self.enter_text(self.LAST_NAME_FIELD, lname)
        self.enter_text(self.PHONE_FIELD, phone)

        scroll_obj.scroll_by(0, 170)
        self.enter_text(self.YEAR_FIELD, year)
        self.enter_text(self.MONTH_FIELD, month)
        self.enter_text(self.DAY_FIELD, day)
        if type.lower() == 'full':
            self.click_operation(self.FULL_TYPE)
        else:
            self.click_operation(self.PROVISIONAL_TYPE)
        self.enter_text(self.LICENCE_PERIOD, licence_period)

        scroll_obj.scroll_by(0, 170)
        self.enter_text(self.OCCUPATION, occupatation)
        self.enter_text(self.STREET, street)
        self.enter_text(self.CITY, city)
        self.enter_text(self.COUNTRY, country)
        self.enter_text(self.PIN_CODE, pin)

        scroll_obj.scroll_by(0, 170)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.enter_text(self.REPASSWORD, password)
    
    def create_account(self):
        self.click_operation(self.CREATE)
        
    
