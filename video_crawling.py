import requests
from bs4 import BeautifulSoup
import time
import urllib.request 
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import datetime as dt
import json

## 유투브 재생을 위한 링크, 제목 크롤링 ##
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options)
driver.get("https://www.youtube.com/")
time.sleep(1)


driver.find_element_by_xpath('//*[@id="search"]')
driver.find_element_by_xpath('//*[@id="search"]').send_keys('KBO 레전드')
driver.find_element_by_xpath('//*[@id="search"]').send_keys(Keys.ENTER)
time.sleep(1)

url = driver.current_url
# url = "https://www.youtube.com/results?search_query=KBO+%EB%A0%88%EC%A0%84%EB%93%9C"
# print(url)
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'lxml')
# print(response)

results = soup.select('h3 > a')
# print(type(results))
result = results[0:10]
# print(results)
kbo_title=[]
kbo_link=[]
kbo_commentlink=[]  ##댓글을 크롤링을 위한 주소
for video in result:
    # print(video)
    # link = video.attrs['href'].replace('/watch?v=','/embed/')
    link = video.attrs['href']  #링크 크롤링
    title = video.attrs['title'] #제목 크롤링
    # print(link, title)
    kbo_commentlink.append(link)
    kbo_link.append(link.replace('/watch?v=','/embed/'))
    kbo_title.append(title)
# print(kbo_link)
# print(kbo_commentlink)    
driver.close()

with open('C:/Users/admin/Documents/mini_project_v2/data/KBO_data-master/Data/kbo_title.json','w', encoding='utf-8') as f:
    json.dump(kbo_title,f)    
with open('C:/Users/admin/Documents/mini_project_v2/data/KBO_data-master/Data/kbo_link.json','w', encoding='utf-8') as g:
    json.dump(kbo_link,g)    


### 유투브 댓글 크롤링 ###
kbo_comments=[]
for li in kbo_commentlink:
    delay = 3
    browser = Chrome()
    browser.implicitly_wait(delay)

    start_url="https://www.youtube.com" + li
    browser.get(start_url)
    browser.maximize_window()
    print(start_url)
    time.sleep(3)
    body = browser.find_element_by_tag_name('body')

    pagedowns = 2  #2번 밑으로
    while pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        pagedowns -= 1
    time.sleep(3)    
    # print('@@@@@@@여기까지 정상')


    html0 = browser.page_source
    soup = BeautifulSoup(html0, 'lxml')

    comment_list = soup.find_all('yt-formatted-string', id='content-text', limit=5)
    comments=[]
    for list in comment_list:
        comment = list.text
        comments.append(comment) # 영상마다 1차 리스트 생성
    print(comments,'@@@1차리스트@@')
    kbo_comments.append(comments) # 영상 다 합쳐서 2차 리스트 생성
    browser.close()
    
print(kbo_comments, '####2차리스트####')


with open('C:/Users/admin/Documents/mini_project_v2/data/KBO_data-master/Data/kbo_comments.json','wt') as h:
    json.dump(kbo_comments,h)       