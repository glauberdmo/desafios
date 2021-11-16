from .reddit_scraper import RedditScraper

def test_redditScraper__get_sub_reddit_html_1():
    '''
    Test the RedditScraper.get_sub_reddit_html() method.
    This method should return a HTML string or None
    Test case 1: for valid subreddits using /r/random
    '''
    #initializes a new RedditScraper object and getting the html for /r/random
    scraper = RedditScraper()
    scraper._get_sub_reddit_html('random')

    #Assure that is a valid page
    not_found_string = "seem to be anything here"
    assert scraper.subreddit_html is not None, 'The subreddit html is None'
    assert  not not_found_string in scraper.subreddit_html, 'The subreddit html is not valid'

def test_redditScraper__get_sub_reddit_html_2():
    '''
    Test the RedditScraper.get_sub_reddit_html() method.
    This method should return a HTML string or None
    Test case 2: for not valid subreddits return none
    '''
    #initializes a new RedditScraper object and getting the html for /r/random
    scraper = RedditScraper()
    scraper._get_sub_reddit_html('fakePageeasdifjg')

    #Assure that is a valid page
    not_found_string = "seem to be anything here"
    assert scraper.subreddit_html =="", 'The subreddit html is not None'



    
