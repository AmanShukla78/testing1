from selenium.webdriver.common.by import By
from base.base_page import BasePage

class DashboardPage(BasePage):
    HEADER = (By.TAG_NAME, "h4")
    
    LINK_HOME=(By.LINK_TEXT,'Home')
    IS_NAVIGATE_HOME=(By.XPATH,'//*[@id="tabs-1"]/h2')
    
    LINK_REQUEST_QUOTE = (By.LINK_TEXT, "Request Quotation")
    IS_NAVIGATE_REQUEST=(By.XPATH,'//*[@id="tabs-2"]/h2')
    
    LINK_RETRIEVE_QUOTE = (By.LINK_TEXT, "Retrieve Quotation")
    IS_NAVIGATE_RETRIEVE = (By.XPATH,'//*[@id="getquote"]')
    
    LINK_PROFILE = (By.LINK_TEXT, "Profile")
    IS_NAVIGATE_PROFILE=(By.XPATH,'//*[@id="tabs-4"]/p[1]/strong')
    
    LINK_EDIT=(By.LINK_TEXT,'Edit Profile')
    IS_NAVIGATE_EDIT=(By.XPATH,'//*[@id="tabs-5"]/h1')
    CLICK_LOGOUT=(By.XPATH,'/html/body/div[3]/form/input')
    LINK_LOGOUT = (By.LINK_TEXT, "Log out")
    LOGOU_VISIBLE=(By.XPATH,"/html/body/div[3]/form/input")

    def is_loaded(self):
        return self.find_web_element(self.HEADER)
    
    def go_home(self):
        self.click_operation(self.LINK_HOME)

    def go_request_quotation(self):
        self.click_operation(self.LINK_REQUEST_QUOTE)

    def go_retrieve_quotation(self):
        self.click_operation(self.LINK_RETRIEVE_QUOTE)

    def go_profile(self):
        self.click_operation(self.LINK_PROFILE)
        
    def go_edit(self):
        self.click_operation(self.LINK_EDIT)

    def logout(self):
        self.click_operation(self.LINK_LOGOUT)
        
    def click_logout(self):
        self.click_operation(self.CLICK_LOGOUT)
        
    def logout_visible(self):
        return self.find_web_element(self.LOGOU_VISIBLE).text
