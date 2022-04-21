# import the urlopen function from the urllib library
import requests

# import the BeautifulSoup function from the bs4 library
from bs4 import BeautifulSoup as bs

# send request to the url
baidu_html = requests.get("http://www.baidu.com")
print(baidu_html.encoding)
print(baidu_html.apparent_encoding)
baidu_html.encoding = "utf-8"

# print out the html string
# print(baidu_html.text)

# parse the html using beautiful soup
parse_baidu = bs(baidu_html.text, "html.parser")

# get the title from <head> then <title>
title = parse_baidu.find('head').find('title').text

# print out the title
print(title) # 百度一下，你就知道

resou_html = requests.get("https://top.baidu.com/board")
resou_html.encoding = "utf-8"

parse_resou = bs(resou_html.text, "html.parser")

# trendingList = parse_resou.find("div", {"class": "theme-hot"}).find_all("div", {"class": "c-single-text-ellipsis"})
for div in parse_resou.find("div", {"class": "theme-hot"}).find_all("div", {"class": "c-single-text-ellipsis"}):
    print(div.text)


