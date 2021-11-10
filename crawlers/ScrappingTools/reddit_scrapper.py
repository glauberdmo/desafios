from bs4 import BeautifulSoup
import requests
import time
from .special_casting import string_to_int_with_k

#Reddit URLs
OLD_REDDIT_URL ='https://old.reddit.com/r/'
NEW_REDDIT_URL = 'https://www.reddit.com'

#Minimum votes to be considered in extraction
VOTES_THRESHOLD = 100 

#HTML tags to find
THREAD_LIST = ['div',{'class': 'thing'}]
THREAD_VOTES = ['div',{'class': 'score likes'}]
THREAD_TITLE = ['p',{'class': 'title'}]
THREAD_LINK = 'data-url'
THREAD_COMMENTS_LINK = 'data-permalink'

#user-Agent - identifies the application making the request, needed for Reddit
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}

class RedditScrapper():
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
            time.sleep(1)
            response = requests.get(OLD_REDDIT_URL+subreddit,headers = USER_AGENT)
            self.subreddit_html = response.text
            if response.status_code == 429:
                print("ERROR: Too many requests")                                
        except Exception as e: 
            print(e)               

    def _getSoup(self,subreddit:str):
        #Gets the soup object
        self.soup = BeautifulSoup(self.subreddit_html,'html.parser')

    def _extract_thread_data(self,soup:object):
        #Gets thread list
        TreadList = soup.find_all(THREAD_LIST[0], THREAD_LIST[1])
        for thread in TreadList:
            thread_votes = string_to_int_with_k(thread.find(THREAD_VOTES[0], THREAD_VOTES[1]).text)

            if thread_votes > VOTES_THRESHOLD:
                title = thread.find(THREAD_TITLE[0], THREAD_TITLE[1]).text
                thread_link = thread.attrs[THREAD_LINK]
                
                #A thread link can be external from reddit
                if '/r/' in thread_link:
                    thread_link = NEW_REDDIT_URL+thread_link 

                thread_comments_link =NEW_REDDIT_URL +  thread.attrs[THREAD_COMMENTS_LINK] #<- always internal link
                self.thread_data.append({'title':title,'votes':thread_votes,'thread_link':thread_link,'comments_link':thread_comments_link})
            else: 
                continue

           
        

