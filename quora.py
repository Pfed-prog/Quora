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
        #self.driver = webdriver.Firefox(executable_path=f'geckodriver') #for debian
        self.driver.get('https://www.quora.com') #opens quora website
        #quora has two different login pages which makes first try invalid from time to time
        try: 
            self.driver.find_element_by_xpath("//input[@placeholder=\'Email\']").send_keys(login)
            self.driver.find_element_by_xpath("//input[@placeholder=\'Password\']").send_keys(password)
            sleep(2) #fixed bug when the login button was clicked too early 
            self.driver.find_element_by_xpath("//input[@value=\'Login\']").click()
            sleep(2) #needed for welcome page to properly initialize
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "root"))) # for welcome to load
        except:
            self.driver.find_element_by_xpath("//input[@placeholder=\"Your email\"]").send_keys(login)
            self.driver.find_element_by_xpath("//input[@placeholder=\"Your password\"]").send_keys(password)
            self.driver.find_element_by_xpath("//button[@tabindex=\"4\"]").click()
            sleep(2)
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "root")))

    def ask(self, category, scroll):
        self.category = category #passes the category name
        self.scroll = scroll #passes the number of scrolls on the page: 1 scroll =10 questions
        self.driver.get("https://www.quora.com/partners?sort_by={}#questions".format(category))#loads the partners page based on the category passed
        low = 0
        high = 10
        #scrolls to load questions; number of scrolls directly targets the range of questions to request (more efficient way fails due to site mechanics)
        if scroll == 0:
            sleep(5)
        elif scroll == 1:
            sleep(4)
            self.driver.execute_script("window.scrollTo(0, 6000)")
            sleep(3)
            low = 10
            high = 20
        elif scroll == 2:
            sleep(2)
            self.driver.execute_script("window.scrollTo(0, 6000)")
            sleep(5)
            self.driver.execute_script("window.scrollTo(0, 6000)")
            sleep(5)
            low = 20
            high = 30
        elif scroll == 3:
            sleep(2)
            self.driver.execute_script("window.scrollTo(0, 6000)")
            sleep(5)
            self.driver.execute_script("window.scrollTo(0, 6000)")
            sleep(5)
            self.driver.execute_script("window.scrollTo(0, 12000)")
            sleep(5)
            low = 30
            high = 40
        else:
            print("number of scrolls - invalid")

        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "questions"))) #confirms loading of questions  
        questions = self.driver.find_element_by_id("questions").find_element_by_class_name("paged_list_wrapper").find_elements_by_class_name("QuestionListItem.partners_question_list_item")    
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "icon_svg-stroke"))) #saves the questions
        for x in range(low, high):
            try:#collects 10 questions
                questions[x].find_element_by_css_selector("div.a2a_section").find_element_by_css_selector("span").click()
                try:
                    try:
                        try:
                            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "q-box.qu-py--small.qu-borderBottom.qu-hover--bg--undefined.qu-tapHighlight--none")))
                            a = self.driver.find_elements_by_class_name("q-box.qu-py--small.qu-borderBottom.qu-hover--bg--undefined.qu-tapHighlight--none")
                            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span")))#collects users
                            for i in range(25):
                                a[i].find_element_by_class_name("q-box.qu-flex--none.qu-display--inline-flex.qu-ml--medium").find_element_by_css_selector("span").click()
                        except:
                            topics = self.driver.find_elements_by_class_name("q-click-wrapper.qu-display--block.qu-tapHighlight--white.qu-cursor--pointer")
                            topics[2].find_element_by_class_name("q-box.qu-py--tiny.qu-hover--bg--undefined.qu-tapHighlight--none").click() #changes topic when there is no suggestions
                            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "q-box.qu-py--small.qu-borderBottom.qu-hover--bg--undefined.qu-tapHighlight--none")))
                            a = self.driver.find_elements_by_class_name("q-box.qu-py--small.qu-borderBottom.qu-hover--bg--undefined.qu-tapHighlight--none")
                            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span")))
                            for i in range(25):
                                a[i].find_element_by_class_name("q-box.qu-flex--none.qu-display--inline-flex.qu-ml--medium").find_element_by_css_selector("span").click()
                    except:        
                        topics[3].find_element_by_class_name("q-box.qu-py--tiny.qu-hover--bg--undefined.qu-tapHighlight--none").click() #changes topic when there is no suggestions
                        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "q-box.qu-py--small.qu-borderBottom.qu-hover--bg--undefined.qu-tapHighlight--none")))
                        a = self.driver.find_elements_by_class_name("q-box.qu-py--small.qu-borderBottom.qu-hover--bg--undefined.qu-tapHighlight--none")
                        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span")))
                        for i in range(25):
                            a[i].find_element_by_class_name("q-box.qu-flex--none.qu-display--inline-flex.qu-ml--medium").find_element_by_css_selector("span").click()
                except:#in case opens question, this closes it
                    self.driver.find_element_by_class_name("q-text.qu-ellipsis.qu-whiteSpace--nowrap").click() #clicks done
            except:#in case not clickable questions - switches to another
                x+=1
    
    def finish(self): #closes the browser
        self.driver.close()

my_bot = Bot('Qwerty@mail.com', 'qwerty') #Enter Creds Here
my_bot.ask('recent', 0)
my_bot.ask('day', 0)
my_bot.ask('week', 0)
my_bot.ask('recent', 1)
my_bot.ask('day', 1)
my_bot.ask('week', 1)
my_bot.ask('day', 2)
my_bot.ask('week', 2)
my_bot.finish()
