# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# R o b o t   |                      Rafael Lapa Valgas
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
# Pageobject Twitter_authentication 
class Authentication():
    def write_login(self, driver, login):
        try: 
            input_login = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")
        except: 
            input_login = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/form/fieldset/div[1]/input')
        input_login.clear()
        input_login.send_keys(login)

    def write_password(self, driver, password):
        try: 
            input_pass = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
        except: 
            input_pass = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/form/fieldset/div[2]/input')
        input_pass.clear()
        input_pass.send_keys(password)

    def click_login_button(self, driver):
        try:
            login_button = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
        except:
            login_button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/form/div[2]/button')
        login_button.click()