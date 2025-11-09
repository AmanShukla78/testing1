from base.base_page import BasePage

class AlertUtil(BasePage):
    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()
    
    def alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text
        