from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# A class for filling text fields and clicking buttons in the sign up form.
class AutomateRegistration:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def automateTextField(self, elementName, text):
        element = self.driver.find_element_by_name(elementName)
        element.clear()
        element.send_keys(text)

    def automateButtonClick(self, className):
        element = self.driver.find_element_by_class_name(className)
        element.send_keys(Keys.RETURN)
