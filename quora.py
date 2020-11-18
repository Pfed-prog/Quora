from selenium import webdriver
from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class Bot:
    
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.driver = webdriver.Chrome(executable_path=f'chromedriver.exe') #loads webdriver
        self.driver.get('https://www.quora.com') #opens quora website
        try:
            self.driver.find_element_by_xpath("//input[@placeholder=\'Email\']").send_keys(login)
            self.driver.find_element_by_xpath("//input[@placeholder=\'Password\']").send_keys(password)
            self.driver.find_element_by_xpath("//input[@value=\'Login\']").click()
            sleep(2)
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "root")))
        except:
            self.driver.find_element_by_xpath("//input[@placeholder=\"Your email\"]").send_keys(login)
            self.driver.find_element_by_xpath("//input[@placeholder=\"Your password\"]").send_keys(password)
            self.driver.find_element_by_xpath("//button[@tabindex=\"4\"]").click()
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "root")))

    def ask(self, category, low, high, scroll):
        self.category = category
        self.low = low
        self.high = high
        self.scroll = scroll  
        self.driver.get("https://www.quora.com/partners?sort_by={}#questions".format(category))
        
        if scroll == 0:
            sleep(5)
        elif scroll == 1:
            sleep(4)
            self.driver.execute_script("window.scrollTo(0, 6000)")
            sleep(3)
        elif scroll == 2:
            sleep(2)
            self.driver.execute_script("window.scrollTo(0, 6000)")
            sleep(5)
            self.driver.execute_script("window.scrollTo(0, 6000)")
            sleep(5)
        else:
            print("number of scrolls - invalid")

        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "questions")))      
        questions = self.driver.find_element_by_id("questions").find_element_by_class_name("paged_list_wrapper").find_elements_by_class_name("QuestionListItem.partners_question_list_item")    
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "icon_svg-stroke")))
        for x in range(low, high):
            try:
                questions[x].find_element_by_css_selector("div.a2a_section").find_element_by_css_selector("span").click()
                try:
                    try:    
                        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "q-box.qu-py--small.qu-borderBottom.qu-hover--bg--undefined.qu-tapHighlight--none")))
                        a = self.driver.find_elements_by_class_name("q-box.qu-py--small.qu-borderBottom.qu-hover--bg--undefined.qu-tapHighlight--none")
                        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span")))
                        self.driver.execute_script("window.scrollTo(0, 500)")
                        for i in range(10):
                            a[i].find_element_by_class_name("q-box.qu-flex--none.qu-display--inline-flex.qu-ml--medium").find_element_by_css_selector("span").click()
                        find_element_by_class_name("q-text.qu-ellipsis.qu-whiteSpace--nowrap").click()
                    except:
                        topics = self.driver.find_elements_by_class_name("q-click-wrapper.qu-display--block.qu-tapHighlight--white.qu-cursor--pointer")
                        #changes topic when there is no suggestions
                        topics[2].find_element_by_class_name("q-box.qu-py--tiny.qu-hover--bg--undefined.qu-tapHighlight--none").click()
                        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "q-box.qu-py--small.qu-borderBottom.qu-hover--bg--undefined.qu-tapHighlight--none")))
                        a = self.driver.find_elements_by_class_name("q-box.qu-py--small.qu-borderBottom.qu-hover--bg--undefined.qu-tapHighlight--none")
                        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span")))
                        self.driver.execute_script("window.scrollTo(0, 500)")
                        for i in range(10):
                            a[i].find_element_by_class_name("q-box.qu-flex--none.qu-display--inline-flex.qu-ml--medium").find_element_by_css_selector("span").click()
                        find_element_by_class_name("q-text.qu-ellipsis.qu-whiteSpace--nowrap").click()
                except:
                    self.driver.find_element_by_class_name("q-text.qu-ellipsis.qu-whiteSpace--nowrap").click()
            except:
                x+=1
    
    def finish(self): #closes the browser
        self.driver.close()

my_bot = Bot('Qwerty@gmail.com', 'Password') #Enter Creds Here
my_bot.ask('recent', 0, 10, 0)
my_bot.ask('day', 0, 10, 0)
my_bot.ask('week', 0, 10, 0)
my_bot.ask('recent', 10, 20, 1)
my_bot.ask('day', 10, 20, 1)
my_bot.ask('week', 10, 20, 1)
my_bot.ask('day', 20, 30, 2)
my_bot.finish()