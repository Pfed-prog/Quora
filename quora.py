from selenium import webdriver
from time import sleep
import argparse

#for future optimization
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.common.by import By
#from selenium.common.exceptions import StaleElementReferenceException


class Bot:
    
    def __init__(self, login, password, category):
        self.login = login
        self.password = password
        self.category = category
        #options = webdriver.ChromeOptions()
        #options.add_argument("start-maximized")
        #options.add_argument("disable-infobars")
        #options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(executable_path=f'chromedriver.exe')
        self.driver.get('https://www.quora.com')
        try:
            self.driver.find_element_by_xpath("//input[@placeholder=\'Email\']").send_keys(login)
            self.driver.find_element_by_xpath("//input[@placeholder=\'Password\']").send_keys(password)
            self.driver.find_element_by_xpath("//input[@value=\'Login\']").click()
        except:
            self.driver.find_element_by_xpath("//input[@placeholder=\"Your email\"]").send_keys(login)
            self.driver.find_element_by_xpath("//input[@placeholder=\"Your password\"]").send_keys(password)
            self.driver.find_element_by_xpath("//button[@tabindex=\"4\"]").click()

    def ask(self):
        sleep(2)
        self.driver.get("https://www.quora.com/partners?sort_by={}#questions".format(self.category))
        sleep(2)
        questions = self.driver.find_element_by_id("questions").find_element_by_class_name("paged_list_wrapper").find_elements_by_class_name("QuestionListItem.partners_question_list_item")    
        self.driver.implicitly_wait(3)
        for x in range(10):
            self.driver.implicitly_wait(2)
            questions[x].find_element_by_css_selector("div.a2a_section").find_element_by_css_selector("span").click()
            self.driver.implicitly_wait(2)
            a = self.driver.find_elements_by_class_name("q-box.qu-py--small.qu-borderBottom.qu-hover--bg--undefined.qu-tapHighlight--none")
            self.driver.implicitly_wait(10)
            try:
                for i in range(25):
                    self.driver.implicitly_wait(1)
                    a[i].find_element_by_class_name("q-box.qu-flex--none.qu-display--inline-flex.qu-ml--medium").find_element_by_css_selector("span").click()
                    
                self.driver.find_element_by_class_name("q-text.qu-ellipsis.qu-whiteSpace--nowrap").click()
            except:
                print('pushing Done')
                self.driver.find_element_by_class_name("q-text.qu-ellipsis.qu-whiteSpace--nowrap").click()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', type=str, help='Email')
    parser.add_argument('-p', type=str, help='Password')
    parser.add_argument('-c', type=str, help='Timeframe', default = 'recent')
    args = parser.parse_args()

    my_bot = Bot(args.e, args.p, args.c)
    my_bot.ask()
