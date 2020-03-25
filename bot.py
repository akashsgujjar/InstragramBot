import time
from lib2to3.pgen2 import driver

from selenium import webdriver

password2 = ''
class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        login1 = self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        login2 = self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath('//button[@type = "submit"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        time.sleep(2)

    def profile(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'{}')]".format(self.username)).click()
        time.sleep(400000)


bot = InstaBot('akashxgujjar', password2)
bot.profile()
