from app.reddit_scraper import RedditScraper
from app.chat_request import *
# uses this file to run through CLI
if __name__=="__main__":
    Scraper = RedditScraper()
    Scraper.get_sub_reddit('rocketleague')
    Scraper.print()



