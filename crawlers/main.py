from reddit_bot.reddit_scraper import RedditScraper

if __name__=="__main__":
    Scraper = RedditScraper()
    Scraper.get_sub_reddit('rocketleague')
    Scraper.print()

