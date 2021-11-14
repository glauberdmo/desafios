import reddit_scraper
import re

#Image used when no hot threads are found
IMAGE_SNOO_SAD = "https://i.redd.it/okvqywqn2jd31.png"

def _get_chat_request(message:str):
    """
    Return valid subreddits and their respective contents
    needs to receive a message in this possible formats:
    /nadaPraFazer | /npf subreddit1 <anySymbolExcept"_"> subreddit2 <anySymbolExcept"_"> subreddit3..
    """
    #get just subreddits
    subreddits = []  
    for sub in message:        
        subreddits.append(re.sub(r'[^\w]', '', sub))

    #subreddits = re.split('; |, |;|,|# |\s+ |- ',"".join(message))
    print(subreddits)
    
    #list of reddits
    reddit_list = []    
    
    #Create scraper object
    Scraper = reddit_scraper.RedditScraper()

    for subreddit in subreddits:
        Scraper.get_sub_reddit(subreddit)

        #verifies if subreddit exists
        if not Scraper.subreddit_exists:
            continue
        else:
            reddit_list.append(Scraper.as_list())
        
    return subreddits, reddit_list

def get_request_result(reddit_list:str)->str:
    answer:list[str] = []
    subreddit_name, subreddits = _get_chat_request(reddit_list)
    if subreddits is not None:
        for i, sub in enumerate(subreddits):
            answer.append(f"<b>{subreddit_name[i]}</b>")
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
        answer.append("Nada bombando no momento" + f"<a href='{IMAGE_SNOO_SAD}'>.</a>")
    return answer
