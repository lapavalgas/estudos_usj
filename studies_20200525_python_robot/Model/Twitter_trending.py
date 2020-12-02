# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# R o b o t   |                      Rafael Lapa Valgas
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Trending():
    def __init__(self, local, hashtag, engagement):
        self.local = local
        self.hashtag = hashtag
        self.engagement = engagement

    def get_trending(self):
            return f"""
Local: {self.local} 
Hashtag: {self.hashtag} 
Engagement: {self.engagement}
---------------------------------------"""