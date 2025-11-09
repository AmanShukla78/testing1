from base.base_page import BasePage
from util.scroll_util import ScrollUtil
from selenium.webdriver.common.by import By

class Profile(BasePage):
    PROFILE_PAGE = (By.XPATH,'//*[@id="ui-id-5"]')
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
    SUBMIT = (By.XPATH,'//*[@id="edit_user_"]/div[14]/input')


    def click_profile(self):
        self.click_operation(self.PROFILE_PAGE)
    
    def user_details(self, title, fname, lname, phone, year, month, day, licence_period, occupatation, street, city, country, pin):
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
    
        self.enter_text(self.LICENCE_PERIOD, licence_period)

        scroll_obj.scroll_by(0, 170)
        self.enter_text(self.OCCUPATION, occupatation)
        self.enter_text(self.STREET, street)
        self.enter_text(self.CITY, city)
        self.enter_text(self.COUNTRY, country)
        self.enter_text(self.PIN_CODE, pin)
    
    def submit(self):
        self.click_operation(self.SUBMIT)