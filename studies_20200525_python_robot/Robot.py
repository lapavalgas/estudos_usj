# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# R o b o t   |                      Rafael Lapa Valgas
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import Model.Twitter
import Model.Instagram
import Resources.robot_data
import Settings.Authentication as user
import time

class Robot():
    def __init__(self):
        # Robot settings
        self.Authentication = user.Authentication()
        # Selenium WebDriver Settings
        self.driver = webdriver.Chrome(executable_path=r'E:\chromedriver.exe')
        self.driver.accept_untrusted_certs = True
        # Robot plugins / Social media
        self.Twitter = Model.Twitter.Twitter(self.Authentication.twitter_user_login)
        self.Instagram = Model.Instagram.Instagram()
        # Robot plugins / behaviors
        # Robot plugins / data mining
        self.data = Resources.robot_data.Data()
        # Open browser

    def open_browser(self, link):
        self.driver.get(link)
    
    def goto_href(self, link):
        self.driver.get(link)