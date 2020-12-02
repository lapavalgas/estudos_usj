# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# R o b o t   |                      Rafael Lapa Valgas
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import Pageobjects.Twitter_authentication as authentication
import Pageobjects.Twitter_tweets as tweet
import Pageobjects.Twitter_post as post
import Pageobjects.Twitter_trendings as trendings
import Resources.robot_data as robot
import time

class Twitter():
    def __init__(self, login):
        # Loading pageobjects
        self.authentication = authentication.Authentication()
        self.post_tweet = post.Twitter_post()
        self.tweet = tweet.Tweet()
        self.trendings = trendings.Trendings()
        # Settings
        self.home = 'https://twitter.com/home'
        self.trendings_home = 'https://twitter.com/explore/tabs/tab_1'
        self.search_engine = 'https://twitter.com/search?q='
        self.profile = f'https://twitter.com/{(login.split("@"))[0]}'
        # Resources
        self.resources = robot.Data()

    def login_authentication(self, driver, login, password):
        self.authentication.write_login(driver, login)
        self.authentication.write_password(driver, password)
        self.authentication.click_login_button(driver)

    def goto_link(self, driver, link, search=''):
        driver.get(link + search)

    def write_tweet_post(self, driver, tweet_text, submit_status):
        self.goto_link(driver, self.home)
        time.sleep(3)
        self.post_tweet.write_tweet_text(driver, tweet_text)
        if submit_status:
            self.post_tweet.submit_tweet_text(driver) 
        else:
            print(f"\nsubmit_status = {submit_status}\nWrite the text:\n{tweet_text},\nbut doesn't sent.")

    def get_tweet_by_link(self, driver, tweet_link, sleep_time=3):
        self.goto_link(driver, tweet_link)
        time.sleep(sleep_time)
        tweet = self.tweet.get_tweet(driver, tweet_link)
        return tweet 

    def get_tweet_list_links(self, driver):
        # Empty list
        tweet_list_links = []
        every_html_href_loaded = self.resources.get_every_html_a_element(driver)
        # Data cleaning 1: catch tweet links
        for html_element in every_html_href_loaded:
            html_element_split = html_element.split('/')
            if 'status' in html_element_split:
                if not len(html_element_split) >= 7:
                    tweet_list_links.append(html_element)
        # Returning tweet list
        return tweet_list_links

    def get_tweet_list_link_by_scrolling(self, driver, scroll_number=2, sleep_time=3):
        # Empty list
        tweet_list = []
        # Scrolling
        time.sleep(sleep_time)
        for i in range(1, scroll_number):
            tweet_list_append = self.get_tweet_list_links(driver) 
            for href in tweet_list_append:
                if not href in tweet_list:
                    tweet_list.append(href)
            self.resources.execute_script(
                driver,
                self.resources.get_script_to_scroll_down_by_pixel(
                    (scroll_number * 1080)
                    )
                )
            time.sleep(sleep_time)
        return tweet_list

    def parse_tweet_list_link_to_Tweet(self, driver, tweet_link_list, sleep_time=3):
        tweet_list = []
        for tweet_link in tweet_link_list:
            tweet_list.append(
                self.get_tweet_by_link(
                    driver,
                    tweet_link,
                    sleep_time
                )
            )
        return tweet_list
    
    def get_trendings_list(self, driver, sleep_time=3):
        # Empty list
        trendings_list = []
        # Getting trendings
        self.goto_link(driver, self.trendings_home)
        time.sleep(sleep_time)
        # Data cleaning 1: catch trending
        for i in range(4, 17):
            trending = self.trendings.get_trending(driver, i)
            #if not trending.hashtag == 'Error xpath':
            trendings_list.append(trending)
        return trendings_list

    def get_trendings_list_links(self, driver):
        # Empty list
        trendings_list_link = []
        every_html_href_loaded = self.resources.get_every_html_a_element(driver)
        # Data cleaning 1: catch trending links
        for html_element in every_html_href_loaded:
            try:
                html_element_split = (html_element.split('?'))[0].split('?')
                if 'search' in html_element_split:
                    if not len(html_element_split) >= 7:
                        trendings_list_link.append(html_element)
            except:
                print('Error to get trendings link')
        return trendings_list_link