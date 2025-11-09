from base.base_page import BasePage
class ScrollUtil(BasePage):
    def scroll_by(self, x=0, y=100):
        self.driver.execute_script(f"window.scrollBy({x}, {y})")
    
    def scrollTo_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  
    
    def scrollTo_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")