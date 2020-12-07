# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# R o b o t   |                      Rafael Lapa Valgas
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import Model.Twitter_tweet as model_tweet
import Resources.robot_data as robot

class Tweet(): 
    def get_tweet(self, driver, link):
        tweet = model_tweet.Tweet(
            self.set_name(driver),
            self.set_profile(driver),
            self.set_data(driver),
            self.set_text(driver),
            link
        )
        return tweet

    def get_text_element_by_xpath(self, driver, xpath):
        try:
            return driver.find_element_by_xpath(xpath).text
        except:
            return 'Erro xpath'

    def set_name(self, driver):
        name_xpaths = [
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/div/div/article/div/div[2]/div[2]/div/div/div/div[1]/a/div/div[1]/div[1]',
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[2]/div[2]/div/div/div/div[1]/a/div/div[1]/div[1]/span/span',
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[2]/div/div/div/div/article/div/div[2]/div[2]/div/div/div/div[1]/a/div/div[1]/div[1]/span/span',
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[2]/div[2]/div/div/div/div[1]/a/div/div[1]',
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[2]/div[2]/div/div/div/div[1]/a/div/div[1]/div[1]',
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[2]/div[2]/div/div/div/div[1]/a/div/div[1]/div[1]/span/span'
        ]
        for xpath in name_xpaths:
            text = self.get_text_element_by_xpath(driver, xpath)
            if not text == 'Erro xpath': 
                return text
            
    def set_profile(self, driver):
        profile_xpath = [
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/div/div/article/div/div[2]/div[2]/div/div/div/div[1]/a/div/div[1]/div[1]',
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[2]/div[2]/div/div/div/div[1]/a/div/div[2]/div/span',
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[2]/div/div/div/div/article/div/div[2]/div[2]/div/div/div/div[1]/a/div/div[2]/div/span',
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[2]/div[2]/div/div/div/div[1]/a/div/div[2]',
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[2]/div[2]/div/div/div/div[1]/a/div/div[2]/div/span',
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[2]/div[2]/div/div/div/div[1]/a/div/div[2]/div/span'
        ]
        for xpath in profile_xpath:
            text = self.get_text_element_by_xpath(driver, xpath)
            if not text == 'Erro xpath': 
                return text
    
    def set_text(self, driver):
        text_xpath = [
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/div/div/article/div/div[3]/div[1]',
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[3]/div[1]',
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[2]/div/div/div/div/article/div/div[3]/div[2]',
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[3]/div[1]',
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[3]/div[1]'
        ]
        for xpath in text_xpath:
            text = self.get_text_element_by_xpath(driver, xpath)
            if not text == 'Erro xpath': 
                return text

    def set_data(self, driver):
        data_xpaths = [
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/div/div/article/div/div[3]/div[3]',
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[3]/div[3]/div/div/span[1]/span',
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[2]/div/div/div/div/article/div/div[3]/div[3]/div/div/span[1]/span',
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[3]/div[3]/div/div/span[1]',
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[3]/div[3]/div/div/span[1]/span',
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div/div[1]/div/div/div/div/article/div/div[3]/div[3]/div/div/span[1]/span'
        ]
        for xpath in data_xpaths:
            text = self.get_text_element_by_xpath(driver, xpath)
            if not text == 'Erro xpath': 
                return text