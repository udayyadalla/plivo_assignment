import sys
import os
import time
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
from elementactions import elementactions
from selenium import webdriver
from Config.Variables import Variables
from Map.Map import Map
from selenium.webdriver import ActionChains

class MyOperations:

    def __init__(self):
        chromedriver = Variables.data['ChromeDriverPath'] 
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.webactions = elementactions(self.driver)
        self.driver.get("http://google.com")
        self.driver.maximize_window()
        object=self.driver.find_element_by_name("q")
        # I have opened the quickfuseapps page here
        self.driver.get("http://quickfuseapps.com/")

    def clickonapp(self):
        try:
            self.driver.find_element_by_xpath(Map.Locators['App']).click()
            time.sleep(3)
            self.driver.find_element_by_xpath(Map.Locators['started']).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(Map.Locators['newpagebutton']).click()
            self.driver.find_element_by_xpath(Map.Locators['newpagetxt']).send_keys(Variables.data['PageName'])
            self.driver.find_element_by_xpath(Map.Locators['Create']).click()
            time.sleep(5)
        except Exception as e:
            raise


    def clickonmessaging(self):
        try:
            self.driver.find_element_by_xpath(Map.Locators['Messaging']).click()
            time.sleep(2)
            source = self.driver.find_element_by_xpath(Map.Locators['sms'])
            ActionChains(self.driver).drag_and_drop_by_offset(source,700,-5).perform()
            time.sleep(5)
            start_node1 = self.driver.find_element_by_xpath(Map.Locators['conector'])
            sms_node2 = self.driver.find_element_by_xpath(Map.Locators['connectorsms'])
            ActionChains(self.driver).drag_and_drop(start_node1,sms_node2).perform()
            time.sleep(2)
            self.driver.find_element_by_xpath(Map.Locators['messagePhnum']).send_keys(Variables.data['PhoneNumber'])
            self.driver.find_element_by_xpath(Map.Locators['messagetext']).send_keys(Variables.data['PageName'])
        except Exception as e:
            raise

    def draganddropsendmail(self):
        try:
            time.sleep(2)
            source_element = self.driver.find_element_by_xpath(Map.Locators['sendmail'])
            time.sleep(2)
            ActionChains(self.driver).drag_and_drop_by_offset(source_element,970,170).perform()
            time.sleep(2)
            self.driver.find_element_by_xpath(Map.Locators['SMTPIp']).send_keys(Variables.data['SMTPHost'])
            self.driver.find_element_by_xpath(Map.Locators['Port']).send_keys(Variables.data['Port'])
            self.driver.find_element_by_xpath(Map.Locators['Username']).send_keys(Variables.data['Username'])
            self.driver.find_element_by_xpath(Map.Locators['passwd']).send_keys(Variables.data['Password'])
            self.driver.find_element_by_xpath(Map.Locators['FromID']).send_keys(Variables.data['From'])
            self.driver.find_element_by_xpath(Map.Locators['ToID']).send_keys(Variables.data['To'])
            self.driver.find_element_by_xpath(Map.Locators['SubID']).send_keys(Variables.data['EmailSubject'])
            self.driver.find_element_by_xpath(Map.Locators['msgID']).send_keys(Variables.data['EmailText'])
            time.sleep(2)
            sms_node3 = self.driver.find_element_by_xpath(Map.Locators['ConnectorEmail'])
            email_node4 = self.driver.find_element_by_xpath(Map.Locators['draggableEmail'])
            ActionChains(self.driver).drag_and_drop(sms_node3,email_node4).perform()
            time.sleep(2)
        except Exception as e:
            raise

    def draganddropExit(self):
        try:
            self.driver.find_element_by_xpath(Map.Locators['Basic']).click()
            exit_element = self.driver.find_element_by_xpath(Map.Locators['Exit']).click()
            time.sleep(2)
            ActionChains(self.driver).drag_and_drop_by_offset(exit_element,470,270).perform()
            time.sleep(5)
            sms_sent_node5 = self.driver.find_element_by_xpath(Map.Locators['sms_sent_node5'])
            exit_node6 = self.driver.find_element_by_xpath(Map.Locators['exit_node6'])
            time.sleep(5)
            ActionChains(self.driver).drag_and_drop(sms_sent_node5,exit_node6).perform()
        except Exception as e:
            raise

    def draganddropExitforemail(self):
        try:
            exit_element = self.driver.find_element_by_xpath(Map.Locators['Exit']).click()
            time.sleep(2)
            ActionChains(self.driver).drag_and_drop_by_offset(exit_element,850,560).perform()
            sent_email_node7 = self.driver.find_element_by_xpath(Map.Locators['sent_email_node7'])
            exit_node8 = self.driver.find_element_by_xpath(Map.Locators['exit_node8'])
            time.sleep(2)
            ActionChains(self.driver).drag_and_drop(sent_email_node7,exit_node8).perform()
            time.sleep(2)
        except Exception as e:
            raise

    def draganddropExitfornotsentemail(self):
        try:
            exit_element_hangup = self.driver.find_element_by_xpath(Map.Locators['Exit']).click()
            ActionChains(self.driver).drag_and_drop_by_offset(exit_element_hangup,1250,560).perform()
            #ActionChains(self.driver).drag_and_drop_by_offset(exit_element,1250,560).perform()
            not_Sent_Email_node9 = self.driver.find_element_by_xpath(Map.Locators['not_Sent_Email_node9'])
            exit_not_node10 = self.driver.find_element_by_xpath(Map.Locators['exit_not_node10'])
            time.sleep(2)
            ActionChains(self.driver).drag_and_drop(not_Sent_Email_node9,exit_not_node10).perform()
            time.sleep(5)
        except Exception as e:
            raise
    
    def shut_down(self):
        '''
            closing the browser
        '''
        self.driver.close()





opr = MyOperations()
opr.clickonapp()
opr.clickonmessaging()
opr.draganddropsendmail()
opr.draganddropExit()
opr.draganddropExitforemail()
opr.draganddropExitfornotsentemail()
opr.shut_down()