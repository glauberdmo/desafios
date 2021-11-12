import reddit_scraper
import re

#Image used when no hot threads are found
IMAGE_SNOO_SAD = "https://i.redd.it/okvqywqn2jd31.png"

def _get_chat_request(message:str)->list[str]:
    """
    Return valid subreddits and their respective contents
    needs to receive a message in the form of:
    /nadaPraFazer subreddit1; subreddit2; subreddit3
    """
    #get just subreddits  
    subreddits = re.split('; |, |;|,|# | |- ',message)[1:]
    
    #list of reddits
    reddit_list = []    
    
    #Create scraper object
    Scraper = reddit_scraper.RedditScraper()

    for subreddit in subreddits:
        Scraper.get_sub_reddit(subreddit)

        #verifies if subreddit exists
        if not Scraper.subreddit_exists:
            continue
        reddit_list.append(Scraper.as_list())
        
    return reddit_list

def get_request_result(reddit_list:str)->str:
    answer:list[str] = []
    subreddits = _get_chat_request(reddit_list)
    if subreddits is not None:
        for sub in subreddits:
            for thread in sub:    
                #avoid adding the same thread link twice when link is not external    
                if 'www.reddit.com' in thread['thread_link']:
                    link_to_comments_HTML = ""    
                else:
                    link_to_comments_HTML = f"<a href='{thread['comments_link']}'> thread comments</a>"
                title_HTML = f"<a href='{thread['thread_link']}'>{thread['title']}</a>"
                votes_HTML = f"<i>Votes:</i> {thread['votes']}"
                answer.append(title_HTML + '\n'+ votes_HTML + '\n'+ link_to_comments_HTML + '\n\n')
    if answer == []:
        answer.append("Nada bombando no momento" + f"<a href='{IMAGE_SNOO_SAD}'>.</a>"
)
    return answer
