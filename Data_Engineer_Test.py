#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import Python Libraries 
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def top_stories(url):
        try:
            print('Connect to Url')
            Client=urlopen(url)
            xml_page=Client.read()
            Client.close()
            print('row data extracted')
        except:
            print('data not extracted')
        try:
            print('Find Top Stories from url')
            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item")

            data=[]
            for news in news_list:
                qut={}
                qut['Top Stories']=news.title.text
                data.append(qut)
            print('data extracted')
        except:
            print('data not extracted')
        try:
            print('convert in dataframe & save in csv')
            stories=pd.DataFrame(data)
            stories.to_csv(r'path\Top_stories.csv',index=False)
            print('csv file stored in location')
        except:
            print('csv file not created')

# Fetch Data putting Url in the funtion of top_stories
            
top_stories('https://www.europarl.europa.eu/rss/doc/top-stories/en.xml')

