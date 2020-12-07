# R o b o t
```
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# R o b o t   |   v 1 . 0 . 0   |   Rafael Lapa Valgas
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
```

## Welcome
Thanks for checking my web scraping study. Here you'll find an selenium based robot that can use the twitter. It can write or retrieve a tweet post, search for tweets, navigate for twitter trending topics and looking for an word in this list. And was programmed to expand with other social medias or websites by plugin-and-play. Is simple and doesn't use regex by now. Well, is based in the page object design pattern, commonly used in selenium projects to test software. But it's finished because an constantly being broken xpaths and a lack of utility. 

I hope this small project can register and demonstrate my programming skills and my code style. Maybe I'll finish this project later writing in Java and developing an RESTful API to controller the robot. Lastly I'll put everything inside an docker.

Really appreciate your time to view, thanks.

## Usage
First you'll need install the dependencies, just run ```pip install -r requirements.txt```. And you'll need the browser driver for selenium, just choose any you like [Geckodrive](https://github.com/mozilla/geckodriver) or [ChromeDriver](https://chromedriver.chromium.org/downloads). Second you'll need configure somethings: In [Robot class](https://github.com/lapavalgas/robot/blob/master/Robot.py) configure your Selenium WebDrive correctly. In [Authentication class](https://github.com/lapavalgas/robot/blob/master/Config/_Authentication.py) you remove the underline and insert user login ans password. Third, know that the [Robot class](https://github.com/lapavalgas/robot/blob/master/Robot.py) implement every behaviour programmed. And the [main](https://github.com/lapavalgas/robot/blob/master/Main.py) is the playground,  that's preserve some scripts i have used to test this program. 

## Contributing
Pull requests with contributions of ideas or to improve my code style are very welcome.

---