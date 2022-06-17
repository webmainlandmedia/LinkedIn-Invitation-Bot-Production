from selenium import webdriver
from core.text_converter import converter
from core.excel_read import filter
import os
import time

CSVFILENAME = 'apollo-contacts-export.csv'
CUSTOMIZE_TEXT = converter('text.txt')


class LinkedIn():
    def __init__(self):
        print("This is an automation message sending bot design for LinkedIn")
        print("Firefox is the defualt web browser for this program.")
        print("Please install Firefox inside of your computer before running the program by visiting https://www.mozilla.org/en-CA/firefox/new/")
        URL = "https://www.linkedin.com/sales/"
        self.USERNAME = input("Please enter your LinkedIn username: ")
        self.PASSWORD = input("Please enter your LinkedIn password: ")
        self.mode = input(
            "Enter RUN for running the bot, OR enter any key for demo: ").upper()
        profile = webdriver.FirefoxProfile()

        profile.set_preference('intl.accept_languages', 'en-US, en')
        # Language preference as English
        self.driver = webdriver.Firefox(firefox_profile=profile,
                                        executable_path=r'.\core\geckodriver.exe')
        self.driver.get(URL)
        # Initailize the web browser and get into the LinkedIn page
        time.sleep(1)

    def login(self):
        # LOGIN SESSION
        username = self.driver.find_element_by_xpath(
            "//input[@name='session_key']")
        password = self.driver.find_element_by_xpath(
            "//input[@name='session_password']")
        username.send_keys(self.USERNAME)
        password.send_keys(self.PASSWORD)
        time.sleep(2)
        submit = self.driver.find_element_by_xpath(
            "//button[@type='submit']").click()
        # Skipping phone number verification step
        try:
            skip = self.driver.find_element_by_xpath(
                "//button[@type='button']").click()
        except:
            print("No Skip Msg!!")

    def msgSending(self):
        self.login()
        data = filter(CSVFILENAME)
        for info in data:
            firstName = info[0]
            link = info[1]
            text = f"Hi {firstName}, {CUSTOMIZE_TEXT}."
            self.driver.get(link)
            time.sleep(2)
            try:
                dot_icon = self.driver.find_element_by_xpath(
                    "//button[starts-with(@id, 'hue-menu-trigger-ember')]").click()
            except:
                print("Could not located the dot icon")
            try:
                connect = self.driver.find_element_by_xpath(
                    "//button[starts-with(@class, 'ember-view')]").click()
            except:
                print("Could not find Connect button")
            time.sleep(1)
            try:
                text_area = self.driver.find_element_by_id(
                    "connect-cta-form__invitation").send_keys(text)
            except:
                print("This user's invitation has been sent out")
            time.sleep(1)
            if self.mode == "RUN":
                try:
                    sendMsg = self.driver.find_element_by_xpath(
                        "//button[starts-with(@class, 'button-primary-medium')]").click()
                except:
                    print("Could not find message sending button")
            time.sleep(1)

    def closeWindow(self):
        # Close window after the automation
        self.driver.close()
        print("The automated session has been done")


def deleteCSVFile(csv_file):
    os.remove(csv_file)


if not os.path.exists(CSVFILENAME):
    print(
        f"Please put '{CSVFILENAME}' in current folder before running the program!!!")
else:
    newtest = LinkedIn()
    time.sleep(5)
    newtest.msgSending()
    time.sleep(2)
    newtest.closeWindow()
    deleteCSVFile(CSVFILENAME)
    print(f"{CSVFILENAME} has been deleted")
