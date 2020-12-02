# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# R o b o t   |                      Rafael Lapa Valgas
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Pageobject write, clear and post tweet
class Twitter_post():
    def write_tweet_text(self, driver, tweet_text):
        try:
            html_input_tweet_text = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
            driver.execute_script(("arguments[0].click()"), html_input_tweet_text)
            html_input_tweet_text.send_keys(tweet_text)
        except:
            print('Erro to write tweet post xpath')
        
    def clear_tweet_text(self, driver):
        return 'not implemented'

    def submit_tweet_text(self, driver):
        try:
            html_button_submit_tweet_post = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/span')
            html_button_submit_tweet_post.click()
        except:
            print('Erro to submit tweet post xpath')