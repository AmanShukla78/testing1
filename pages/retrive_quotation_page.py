from selenium.webdriver.common.by import By
from base.base_page import BasePage

class RetrieveQuotationPage(BasePage):
    QUOTE_ID = (By.XPATH,'//*[@id="tabs-3"]/form/input[1]')
    RETRIEVE_BTN = (By.XPATH, '//*[@id="getquote"]')
    RESULT = (By.XPATH, "/html/body/table/tbody")
    WRONG_MSG=(By.XPATH,'/html/body/b')

    def retrieve(self, quote_id: str):
        self.remove_enter_text(self.QUOTE_ID, quote_id)
        self.click_operation(self.RETRIEVE_BTN)
        
    def res(self):
        return self.find_web_element(self.RESULT).text

    def result_present(self):
        return self.exists(self.RESULT)
    
    def get_error_msg(self):
        return self.find_web_element(self.WRONG_MSG).text