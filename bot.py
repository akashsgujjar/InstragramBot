import time
from lib2to3.pgen2 import driver
from selenium import webdriver
from pynput.keyboard import Key, Controller

password2 = input("password: ")


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

    def scroll(self):
        keyboard = Controller()
        self.driver.get("ADD_LINK_HERE")
        for loop in range(100):
            try:
                self.driver.find_element_by_xpath("//textarea[@class=\"Ypffh\"]").send_keys("yoohoo")
            except:
                keyboard.type("yoohoo")
                time.sleep(2)
                self.driver.find_element_by_xpath('//button[@type = "submit"]').click()
                time.sleep(2)

        time.sleep(40000)


bot = InstaBot('akashofclans', password2)
bot.scroll()
