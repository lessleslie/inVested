import feedparser
import requests
import webbrowser 
import nltk
from newspaper import Article
import urllib.request
from bs4 import BeautifulSoup


class article: 

    def __init_(self): 
        self.title = ""
        self.link = "" 
        self.content= "" 
    
    def parseContent(self): 
        self.content = ""
        parsePage = requests.get(self.link)
        soup = BeautifulSoup(parsePage.text, 'html.parser')
        for el in soup.find_all("div", {"class": "zn-body__paragraph speakable"}):
            self.content+=el.get_text()
        return self.content

class scraperRSS: 

    def __init__(self, rssLink): 

        self.rssLink = rssLink
        self.posts = []

    def parseRSS(self):

        feed = feedparser.parse('http://rss.cnn.com/rss/money_news_companies.rss')
        if feed.status == 200:
            numberOfHeadlines = len(feed['entries'])

            for i in range(0,numberOfHeadlines):
                currentArticle = article()
                currentArticle.title = feed['entries'][i].title
                currentArticle.link = feed['entries'][i].link
                currentArticle.date = feed['entries'][i].published
                currentArticle.content = currentArticle.parseContent()
                self.posts.append(currentArticle)
            return self.posts
        else:
            print("Some connection error", feed.status)
    
scrapeCNN = scraperRSS('http://rss.cnn.com/rss/money_news_companies.rss')
# print(scrapeCNN.parseRSS()[0].content)


