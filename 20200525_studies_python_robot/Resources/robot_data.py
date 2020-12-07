# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# R o b o t   |                      Rafael Lapa Valgas
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

class Data():
    def execute_script(self, driver, script):
        driver.execute_script(script)

    def get_script_to_scroll_down_by_pixel(self, pixels):
       return f"window.scrollTo(0, {pixels});"

    def get_every_html_a_element(self, driver):
        # Getting html a hrefs
        every_html_a_href_loaded = driver.find_elements_by_xpath("//a[@href]")
        every_html_href_loaded = []
        # Data cleaning 1 : catch href from every a html element
        for hrefs in every_html_a_href_loaded:
            every_html_href_loaded.append(hrefs.get_attribute('href'))
        return every_html_href_loaded

    def tweet_post_to_text_list(self, tweet_post):
        return tweet_post.split()

    def search_an_word_in_tweet_text_list(self, word, tweet_text_list):
        if word in tweet_text_list:
            return True
        else:
            return False