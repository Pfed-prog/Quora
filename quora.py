from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import argparse

class Bot:
    def __init__(self, login, password):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        #enter your driver path
        self.browser = webdriver.Chrome(chrome_options=options, executable_path=r'C:\webdrivers\chromedriver.exe')
        self.login = login
        self.browser.get('https://www.quora.com')
        sleep(5)
        self.browser.find_element_by_xpath("//input[@placeholder=\'Email\']")\
            .send_keys(login)
        sleep(2)
        self.browser.find_element_by_xpath("//input[@placeholder=\'Password\']")\
            .send_keys(password)
        sleep(2)
        self.browser.find_element_by_xpath("//input[@value=\'Login\']")\
            .click()
        sleep(2)
        self.browser.get('https://www.quora.com/partners?sort_by=day#questions')
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', type=str, help='Email')
    parser.add_argument('-p', type=str, help='Password')
 
    args = parser.parse_args()

    Bot(args.e, args.p)