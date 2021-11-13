from bs4 import BeautifulSoup
import requests
import time


#Reddit URLs
OLD_REDDIT_URL ='https://old.reddit.com/r/'
NEW_REDDIT_URL = 'https://www.reddit.com'

#Minimum votes to be considered in extraction
VOTES_THRESHOLD = 5000 

#HTML tags to find
THREAD_LIST = ['div',{'class': 'thing'}]
THREAD_VOTES = ['div',{'class': 'score likes'}]
THREAD_TITLE = ['p',{'class': 'title'}]
THREAD_LINK = 'data-url'
THREAD_COMMENTS_LINK = 'data-permalink'

#user-Agent - identifies the application making the request, needed for Reddit
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}

class RedditScraper():
    def __init__(self):
        self.subreddit_html = ""
        self.soup:object = None
        self.thread_data = []
        
    def print(self):
        for thread in self.thread_data:
            print(f"Thread: {thread['title']}")
            print(f"Votes received: {thread['votes']}")
            print(f"Thread link: {thread['thread_link']}")
            print(f"Thread comments link: {thread['comments_link']}" + "\n")
    
    def __getittem__(self,index:int):
        return self.thread_data[index]

    def as_list(self):
        return self.thread_data

    def subreddit_exists(self):
        return len(self.thread_data) > 0

    def get_sub_reddit(self,subreddit:str):
        #Gets the subreddit HTML
        self._get_sub_reddit_html(subreddit)

        #Parses the HTML
        self._getSoup(subreddit)

        #Extracts the thread data
        self._extract_thread_data(self.soup)      

    def _get_sub_reddit_html(self,subreddit:str):
        #Requests the subreddit
        try:
            time.sleep(2)
            response = requests.get(OLD_REDDIT_URL+subreddit,headers = USER_AGENT)
            self.subreddit_html = response.text
            if response.status_code == 429:
                print("ERROR: Too many requests")
        except Exception as e: 
            print(e)               

    def _getSoup(self,subreddit:str):
        #Gets the soup object
        self.soup = BeautifulSoup(self.subreddit_html,'html.parser')
    

    def _format_votes(self,str_number)->int:        
        #Solve possible formating issues getting votes.        
        if str_number == '•' or str_number == None:
            return 0 
        elif str_number.endswith('k'):
            str_number = str_number[:-1]
            return int(str_number.replace('.', '')) * 100
        else:
            return int(str_number)

    def _extract_thread_data(self,soup:object)->bool:
        #Gets thread list
        TreadList = soup.find_all(THREAD_LIST[0], THREAD_LIST[1])

        if TreadList == None:
            print("ERROR: No threads found, subrredit invalid")
            self.thread_data = []
            return

        for thread in TreadList:
            thread_votes = self._format_votes(thread.find(THREAD_VOTES[0], THREAD_VOTES[1]).text)
            a = thread.find(THREAD_TITLE[0], THREAD_TITLE[1])
            if thread_votes > VOTES_THRESHOLD:
                title = thread.find(THREAD_TITLE[0], THREAD_TITLE[1]).text
                thread_link = thread.attrs[THREAD_LINK]
                
                #A thread link can be external from reddit
                if '/r/' in thread_link:
                    thread_link = NEW_REDDIT_URL+thread_link 

                thread_comments_link =NEW_REDDIT_URL +  thread.attrs[THREAD_COMMENTS_LINK]
                self.thread_data.append({'title':title,'votes':thread_votes,'thread_link':thread_link,'comments_link':thread_comments_link})
            else: 
                continue