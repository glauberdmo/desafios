from ScrappingTools.reddit_scrapper import RedditScrapper

if __name__=="__main__":
    scrapper = RedditScrapper()
    scrapper.get_sub_reddit('askscience')
    scrapper.print()

