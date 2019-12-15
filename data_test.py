from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

url = 'https://www.daum.net'

# 크롬창 안띄우고 실행하는 옵션 추가
chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome('/home/vscode/myproject/miniproject/chromedriver', options = chrome_options)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

items = soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li')

for item in items:
    rank = item.find('span', class_ = 'ir_wa').text
    keyword = item.find('span', attrs = {'class': 'txt_issue'}).text

    print('rank:', rank)
    print('keyword:', keyword)