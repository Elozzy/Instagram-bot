from selenium import webdriver
import os
import time
import configparser

class InstagramBot:

    def __init__(self, username, password):
        """
        Argss:
            username:str: YOur username
            password:str: Your instagram password
        """
        self.username = username
        self.password = password
        self.base_url = "https://www.instagram.com"
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.login()

      

    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))


        

    def login(self):
        self.driver.get('{}'.format(self.base_url))
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        #self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()

        time.sleep(4)

    def follow_user(self, user):
        self.nav_user(user)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        follow_button.click()

    def unfollow_user(self, user):
        self.nav_user(user)
        unfollow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Following')]")[0]
        follow_button.click()


if __name__ == '__main__':

    config_path = './config_.ini'
    cparser = configparser.ConfigParser()
    cparser.read(config_path)
    username = cparser['AUTH']['USERNAME']
    password =cparser['AUTH']['PASSWORD']

    ig_bot = InstagramBot(username, password)
    ig_bot.follow_user('INPUT USERNAME TO FOLLOW')



    
