from reddit_bot.reddit_scraper import RedditScraper

# uses this file to run through CLI
if __name__=="__main__":
    Scraper = RedditScraper()
    Scraper.get_sub_reddit('rocketleague')
    Scraper.print()

