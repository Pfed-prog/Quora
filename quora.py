from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import argparse

path = 'C:\webdrivers\chromedriver.exe'

class Bot:
    def __init__(self, login, password):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        self.browser = webdriver.Chrome(options=options, executable_path=path)
        self.login = login
        self.browser.get('https://www.quora.com')
        try:
            self.browser.find_element_by_xpath("//input[@placeholder=\'Email\']").send_keys(login)
            self.browser.find_element_by_xpath("//input[@placeholder=\'Password\']").send_keys(password)
            self.browser.find_element_by_xpath("//input[@value=\'Login\']").click()
        except:
            print('firstExcept')
            self.browser.find_element_by_xpath("//input[@placeholder=\"Your email\"]").send_keys(login)
            self.browser.find_element_by_xpath("//input[@placeholder=\"Your password\"]").send_keys(password)
            self.browser.find_element_by_xpath("//button[@tabindex=\"4\"]").click()

        sleep(2)
        self.browser.get("https://www.quora.com/partners?sort_by=day#questions")
        sleep(2)
        questions = self.browser.find_element_by_id("questions").find_element_by_css_selector("div.paged_list_wrapper").find_elements_by_css_selector("div.QuestionListItem")
        sleep(3)
        for x in range(10):
            try:
                questions[x].find_element_by_css_selector("div.a2a_section").find_element_by_css_selector("span").click()
                sleep(6)
                a = self.browser.find_elements_by_class_name("q-box.qu-py--small.qu-borderBottom.qu-hover--bg--undefined.qu-tapHighlight--none")

                try:
                    for i in range(25):
                        print(i)
                        a[i].find_element_by_class_name("q-box.qu-flex--none.qu-display--inline-flex.qu-ml--medium").find_element_by_css_selector("span").click()
    
                except:
                    self.browser.find_element_by_class_name("q-text.qu-ellipsis.qu-whiteSpace--nowrap").click()
            except:
                print('bad'+str(x))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', type=str, help='Email')
    parser.add_argument('-p', type=str, help='Password')
    args = parser.parse_args()

    my_bot = Bot(args.e, args.p)
