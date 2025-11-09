from selenium.webdriver.common.by import By
from util.scroll_util import ScrollUtil
from base.base_page import BasePage

class RequestQuotationPage(BasePage):
    BREAKDOWN = (By.ID, "quotation_breakdowncover")
    WINDSCREEN_YES = (By.ID, "quotation_windscreenrepair_t")
    WINDSCREEN_NO = (By.ID, "quotation_windscreenrepair_f")
    INCIDENTS = (By.ID, "quotation_incidents")
    REGISTRATION = (By.ID, "quotation_vehicle_attributes_registration")
    MILEAGE = (By.ID, "quotation_vehicle_attributes_mileage")
    VALUE = (By.ID, "quotation_vehicle_attributes_value")
    PARKING = (By.ID, "quotation_vehicle_attributes_parkinglocation")
    POL_START = (By.ID, "quotation_vehicle_attributes_policystart_1i")
    POL_MONTH = (By.ID, "quotation_vehicle_attributes_policystart_2i")
    POL_DAY = (By.ID, "quotation_vehicle_attributes_policystart_3i")
    CALCULATE = (By.NAME, "submit")
    SAVE = (By.XPATH, "//input[@value='Save Quotation']")
    CONFIRM = (By.XPATH, "/html/body/b[1]")
    QUOTATION_NUMBER=(By.XPATH,'/html/body/b[2]')

    def fill_valid_quote(self,breakdown,parking,y,m,d):
        scroll_obj = ScrollUtil(self.driver)
        scroll_obj.scroll_by(0, 170)
        self.enter_text(self.BREAKDOWN,breakdown)
        self.click_operation(self.WINDSCREEN_YES)
        self.remove_enter_text(self.INCIDENTS, "No incidents")
        self.remove_enter_text(self.REGISTRATION, "TEST123")
        self.remove_enter_text(self.MILEAGE, "10000")
        self.remove_enter_text(self.VALUE, "5000")
        
        scroll_obj.scroll_by(0, 350)
        self.enter_text(self.PARKING,parking)
        self.enter_text(self.POL_START,y)
        self.enter_text(self.POL_MONTH,m)
        self.enter_text(self.POL_DAY,d)
        

    def calculate(self):
        self.click_operation(self.CALCULATE)

    def save(self):
        self.click_operation(self.SAVE)
        
    def success_msg(self):
        return self.find_web_element(self.CONFIRM).text
    
    def quotation_number(self):
        return self.exists(self.QUOTATION_NUMBER)

    def confirmation_present(self):
        return self.exists(self.CONFIRM)
