# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# R o b o t   |                      Rafael Lapa Valgas
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import Model.Twitter
import Model.Instagram
import Resources.robot_data
import Pageobjects.Twitter_authentication as auth
import Pageobjects.Twitter_tweets as tweet
import Pageobjects.Twitter_post as post
import Pageobjects.Twitter_trendings as trendings
import Resources.robot_data as robot
import Robot as turn_on

def printlog_simple(somethinga, somethingb):
    print('\n\n-----------------------------')
    print(f'{somethinga}\n{somethingb}')
    print('-----------------------------')

def printlog_twitter(somethinga, somethingb):
    print(f'\n\n{somethinga}\n{somethingb}')

robot = turn_on.Robot()

robot.open_browser(
    'https://twitter.com/login'
)

robot.Twitter.login_authentication(
    robot.driver,
    robot.Authentication.twitter_user_login,
    robot.Authentication.twitter_user_password
    ) 

robot.Twitter.write_tweet_post(
    robot.driver,
    """# R o b o t   |   v 1 . 0 . 0   |   Rafael Lapa Valgas""",
    False
)

tweet_list_link = robot.Twitter.get_tweet_list_link_by_scrolling(
    robot.driver,
    2
)

printlog_simple('tweet_list_link', tweet_list_link)

tweet_list = robot.Twitter.parse_tweet_list_link_to_Tweet(
    robot.driver,
    tweet_list_link
)

printlog_simple('tweet_list', tweet_list)

for tweet in tweet_list: 
    printlog_twitter('tweet', tweet.get_tweet())
    #Still working, but the DOMs continuously updating, I can't be updating this without an good reason or use for this robot. The logic works, go to Pageobject.Twitter_tweet and update xpath by your own.

trendings_list = robot.Twitter.get_trendings_list(
    robot.driver
)

printlog_simple('tweet_list', trendings_list)

for trending in trendings_list: 
     printlog_twitter('tweet', trending.get_trending())

for trending in trendings_list: 

    printlog_simple('Getting trendings', trending.get_trending())

    if not trending.hashtag == None:
        hashtag = trending.hashtag.split('#') 
        hashtag = ''.join(hashtag)

        robot.Twitter.goto_link(
            robot.driver,
            robot.Twitter.search_engine,
            hashtag
        )

        tweet_list_link = robot.Twitter.get_tweet_list_link_by_scrolling(
            robot.driver,
            2
        )

        tweet_list = robot.Twitter.parse_tweet_list_link_to_Tweet(
            robot.driver,
            tweet_list_link
        )

        for tweet in tweet_list: 
            printlog_twitter('tweet', tweet.get_tweet())

robot.open_browser(
    robot.Twitter.profile
    )