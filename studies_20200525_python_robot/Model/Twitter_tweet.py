# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# R o b o t   |                      Rafael Lapa Valgas
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Tweet():
    def __init__(self, name, profile, data, text, link):        
        # Mounting data
        self.name = name
        self.profile = profile
        self.data = data
        self.text = text
        self.link = link

    def get_tweet(self):
        return f"""
Name: {self.name}  / profile: {self.profile}  /  data: {self.data}

Text: {self.text}

Link: {self.link} 
--------------------------------------------------------------------"""