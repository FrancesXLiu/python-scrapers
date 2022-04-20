# import the urlopen function from the urllib library
import requests

# import the BeautifulSoup function from the bs4 library
from bs4 import BeautifulSoup as bs

# send request to the url
html = requests.get("http://www.baidu.com")
print(html.encoding)
print(html.apparent_encoding)
html.encoding = "utf-8"

# print out the html string
print(html.text)

# parse the html using beautiful soup
parse_html = bs(html.text, "html.parser")

# get the title from <head> then <title>
title = parse_html.find('head').find('title').text

# print out the title
print(title) # 百度一下，你就知道

#s_xmancard_news_new > div > div.s-news-rank-wrapper.s-news-special-rank-wrapper.c-container-r > div > div > ul
trendingList = parse_html.find("ul", {"class": "s-news-rank-content"}) # 热搜不在百度首页，需要request热搜的网址

print(trendingList)
