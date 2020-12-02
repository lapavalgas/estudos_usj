# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# R o b o t   |                      Rafael Lapa Valgas
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import Model.Twitter_trending as model_trending

class Trendings():
    def get_trending(self, driver, number):
        trending = model_trending.Trending(
            self.set_local(driver, number),
            self.set_hashtag(driver, number),
            self.set_engagement(driver, number)
        )
        return trending

    def get_text_element_by_xpath(self, driver, xpath):
        try:
            return driver.find_element_by_xpath(xpath).text
        except:
            return 'Erro xpath'

    def set_local(self, driver, number):
        local_xpaths = [
            f'/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[{number}]/div/div/div/div[1]',
            f'/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div/div[{number}]/div/div/div/div[1]/div/span',
            f'/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div/div[{number}]/div/a/div[1]/div[1]/div[1]/span'
        ]
        for xpath in local_xpaths:
            text = self.get_text_element_by_xpath(driver, xpath)
            if not text == 'Erro xpath': 
                return text

    def set_hashtag(self, driver, number):
        hashtag_xpath = [
            f'/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[{number}]/div/div/div/div[2]',
            f'/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div/div[{number}]/div/div/div/div[2]/span',
            f'/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div/div[{number}]/div/a/div[1]/div[2]'
        ]
        for xpath in hashtag_xpath:
            text = self.get_text_element_by_xpath(driver, xpath)
            if not text == 'Erro xpath': 
                return text

    def set_engagement(self, driver, number):
        engagement_xpath = [
            f'/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[{number}]/div/div/div/div[3]',
            f'/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div/div[{number}]/div/div/div/div[3]/span'
        ]
        for xpath in engagement_xpath:
            text = self.get_text_element_by_xpath(driver, xpath)
            if not text == 'Erro xpath': 
                return text