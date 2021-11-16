import re

import reddit_scraper



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
    subreddits_not_flat = []
    for sub in message:        
        subreddits_not_flat.append(re.split(r'[^\w]', sub))
    
    # appending elements to the flat_list
    for sub in subreddits_not_flat:  
        subreddits += sub
    #removing '' from the list
    for sub in subreddits:
        if sub == '':
            subreddits.remove(sub)

    #list of reddits
    reddit_list = []    
    
    #Create scraper object
    Scraper = reddit_scraper.RedditScraper()

    for i, subreddit in enumerate(subreddits):
        Scraper.get_sub_reddit(subreddit)

        #verifies if subreddit exists
        if not Scraper.subreddit_exists():
            subreddits[i] += " does not exist!"
            reddit_list.append({'title':subreddits[i],'votes':"",'thread_link':"",'comments_link':""})
        else:
            if not Scraper.hot_thread_exists():
                subreddits[i] += " does not have hot threads"
                reddit_list.append({'title':subreddits[i],'votes':"",'thread_link':"",'comments_link':""})
            else:
                reddit_list.append(Scraper.as_list())

    return subreddits, reddit_list

def get_request_result(reddit_list:str)->str:
    answer:list[str] = []
    subreddit_name, subreddits_content = _get_chat_request(reddit_list)
    for i, sub in enumerate(subreddits_content):
        answer.append(f"<b>{subreddit_name[i]}</b>")
        if "does not exist" in subreddit_name[i] or "does not have hot threads" in subreddit_name[i]:
            continue
        else:
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

