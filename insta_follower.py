import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

TARGET_ACCOUNT = 'chefsteps'
INSTAGRAM_URL = "https://www.instagram.com/"
MY_INSTAGRAM_ACCT = "rustleup2"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 30)

    def login(self, user, pw):
        # url = "https://www.instagram.com/login/"
        url = INSTAGRAM_URL+MY_INSTAGRAM_ACCT
        self.driver.get(url)

        # Agree to essential cookies
        gdpr_button = self.driver.find_element(By.XPATH, "/ html / body / div[4] / div / div / button[1]")
        gdpr_button.click()

        time.sleep(10)

        # Suddenly, the login screen changed and now requires a login button
        # be pressed to enter credentials.
        try:
            # Enter username
            username_input = self.driver.find_element(By.NAME, "username")
        except "NoSuchElementException":
            login_button = self.driver.find_element(By.LINK_TEXT, "Log in")
            login_button.click()
        else:
            username_input.click()
            username_input.send_keys(user)

            # Enter password
            password_input = self.driver.find_element(By.NAME, "password")
            password_input.click()
            password_input.send_keys(pw)
            password_input.send_keys(Keys.TAB + Keys.TAB + Keys.ENTER)

        # Don't save login
        not_now_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")))
        not_now_button.click()


    def find_followers(self):
        # Load the target account
        url = INSTAGRAM_URL+TARGET_ACCOUNT
        self.driver.get(url)

        time.sleep(15)

        # Click the followers link
        followers_link = self.driver.find_element(By.CSS_SELECTOR, "li.Y8-fY:nth-child(2) > a:nth-child(1) > div:nth-child(1)")
        followers_link.click()


    def follow(self):
        pass
