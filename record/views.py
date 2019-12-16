from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .models import Record
from .models import Pitcher
from .models import Team
from .models import Hitter
import json
import sqlite3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib.request, time


# Create your views here.
def recordList(request):
    if request.method == "GET":
        # json 파일 내용 DB 에 insert
        # with open ("C:/Users/admin/Documents/mini_project_v2/data/KBO_data-master/Data/KBO_2016_season.json", 'r', encoding='utf-8') as json_file:
        #     dataList = json.load(json_file)

        # for data in dataList: 
        #     date = data['Date']
        #     gujang = data['구장']
        #     away_team = data['원정팀']
        #     away_point = data['원정팀점수']
        #     home_point = data['홈팀점수']
        #     home_team = data['홈팀']
        #     away_result = data['원정팀결과']
        #     home_result = data['홈팀결과']
        #     etc = data['비고']

        #     record = Record(rcd_date=date, rcd_gujang=gujang, rcd_awayteam=away_team, rcd_awaypoint=away_point, rcd_homepoint=home_point, rcd_hometeam=home_team, rcd_awayresult=away_result, rcd_homeresult=home_result, rcd_etc=etc)
        #     record.save()

        searchYear = request.GET.get('searchYear', '')
        searchMonth = request.GET.get('searchMonth', '')

        searchKeyword = ''

        if searchYear != '':
            searchKeyword = searchYear

        if searchYear != '' and searchMonth != '':
            searchKeyword = searchYear + '-' + searchMonth

        recordList = Record.objects.filter(rcd_date__icontains = searchKeyword).order_by('-rcd_date')  

        paginator = Paginator(recordList, 15)
        page = request.GET.get('page', 1)
        posts = paginator.get_page(page)

        return render(request, 'record/recordList.html', {'recordList': recordList, 'posts': posts, 'searchYear': searchYear, 'searchMonth': searchMonth})

def pitcherList(request):
    if request.method == "GET":
        # json 파일 내용 db에 insert
        # with open ("C:/Users/admin/Documents/mini_project_v2/data/KBO_data-master/Data/pitcher.json",'r',encoding='utf-8') as json_file:
        #     datalist = json.load(json_file)
    
        # for data in datalist:
        #     p_no   = data['순위']
        #     p_name = data['선수명']
        #     p_team = data['팀명']
        #     p_era  = data['ERA']
        #     p_game = data['G']
        #     p_win  = data['W']
        #     p_lose = data['L']
        #     p_sv   = data['SV']
        #     p_hld  = data['HLD']
        #     p_wpct = data['WPCT']
        #     p_ip   = data['IP']
        #     p_h    = data['H']
        #     p_hr   = data['HR']
        #     p_bb   = data['BB']
        #     p_hbp  = data['HBP']
        #     p_so   = data['SO']
        #     p_r    = data['R']
        #     p_er   = data['ER']
        #     p_whip = data['WHIP']
            
        #     pitcher = Pitcher(p_no=p_no,p_name=p_name,p_team=p_team,p_era=p_era,p_game=p_game,p_win=p_win,p_lose=p_lose,p_sv=p_sv,p_hld=p_hld,p_wpct=p_wpct,p_ip=p_ip,p_h=p_h,p_hr=p_hr,p_bb=p_bb,p_hbp=p_hbp,p_so=p_so,p_r=p_r,p_er=p_er,p_whip=p_whip)
        #     pitcher.save()

        searchtype = request.GET.get('type','')
        searchkeyword = request.GET.get('text','')
        if searchtype == 'p_team':
            pitcherList = Pitcher.objects.filter(p_team__icontains=searchkeyword).order_by('p_team')
            
        elif searchtype == 'p_name':
            pitcherList = Pitcher.objects.filter(p_name__icontains=searchkeyword).order_by('p_team')

        if searchtype == '' and searchkeyword == '':
            pitcherList = Pitcher.objects.raw('SELECT * FROM RECORD_PITCHER WHERE (CAST(P_IP as INTEGER) >= 144) ORDER BY P_ERA')

        paginator = Paginator(pitcherList, 15)
        page = request.GET.get('page', 1)
        posts = paginator.get_page(page)

        return render(request, 'record/pitcherList.html', {'pitcherList': pitcherList, 'posts': posts, 'searchtype':searchtype, 'searchkeyword':searchkeyword})

def hitterList(request):
    if request.method == "GET":
        # json 파일 내용 db에 insert
        # with open ("C:/Users/admin/Documents/mini_project_v2/data/KBO_data-master/Data/hitter.json",'r',encoding='utf-8') as json_file:
        #     datalist = json.load(json_file)

        # for data in datalist:
        #     h_no = data['순위']
        #     h_name = data['선수명']
        #     h_team = data['팀명']
        #     h_avg = data['AVG']
        #     h_game = data['G']
        #     h_pa = data['PA']
        #     h_ab = data['AB']
        #     h_r = data['R']
        #     h_h = data['H']
        #     h_2b = data['2B']
        #     h_3b = data['3B']
        #     h_hr = data['HR']
        #     h_tb = data['TB']
        #     h_rbi = data['RBI']
        #     h_sac = data['SAC']
        #     h_sf = data['SF']
            
        #     hitter = Hitter(h_no=h_no, h_name=h_name, h_team=h_team, h_avg=h_avg, h_game=h_game, h_pa=h_pa, h_ab=h_ab, h_r=h_r, h_h=h_h, h_2b=h_2b, h_3b=h_3b, h_hr=h_hr, h_tb=h_tb, h_rbi=h_rbi, h_sac=h_sac, h_sf=h_sf)
        #     hitter.save()

        searchtype = request.GET.get('type','')
        searchkeyword = request.GET.get('text','')
        if searchtype == 'h_team':
            hitterList = Hitter.objects.filter(h_team__icontains=searchkeyword).order_by('h_team', '-h_avg')
            # print(hitterList, "@@@@@@@@@@@@")
        elif searchtype == 'h_name':
            hitterList = Hitter.objects.filter(h_name__icontains=searchkeyword).order_by('h_team', '-h_avg')

        if searchtype == '' and searchkeyword == '':
            hitterList = Hitter.objects.raw('SELECT * FROM RECORD_HITTER WHERE (CAST(H_PA as INTEGER) >= 446) ORDER BY H_AVG DESC')

        paginator = Paginator(hitterList, 15)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        pageList = []

        for i in range(1, paginator.num_pages + 1, 1):
            pageList.append(i)

        return render(request, 'record/hitterList.html', {'hitterList' : hitterList, 'posts':posts, 'pageList':pageList, 'searchtype':searchtype, 'searchkeyword':searchkeyword})

@csrf_exempt
def teamyear(request):
    if request.method =='GET':
        # json 파일 내용 db에 insert
       

        search_year = request.GET.get('search_year','2019')

        if search_year != "":
            teamList = Team.objects.filter(t_year=search_year).order_by('t_no')
        
        else:
            teamList = Team.objects.filter(t_year='2019').order_by('t_no')
            search_year = 2019

        return render(request, 'record/teamyear.html',{'teamList':teamList, 't_year':search_year})

    # if request.method == "POST":
    #     with open ("C:/Users/admin/Documents/mini_project_v2/data/KBO_data-master/Data/rankteam.json",'r',encoding='utf-8') as json_file:
    #         datalist = json.load(json_file)

    #     for data in datalist:
    

    #         t_chai = data['게임차']
    #         t_10   = data['최근10경기']
    #         t_cont = data['연속']
    #         t_home = data['홈']
    #         t_away = data['방문']
    #         t_year = data['연도']
            
    #         teamyear = Team(t_no=t_no,t_name=t_name,t_game=t_game,t_win=t_win,t_lose=t_lose,t_draw=t_draw,t_per=t_per,t_chai=t_chai,t_10=t_10,t_cont=t_cont,t_home=t_home,t_away=t_away,t_year=t_year )
    #         teamyear.save()

        # return 0    
            
import matplotlib.pyplot as plt #그래프그리기
from matplotlib import font_manager, rc #한글적용폰트설정
import io #그래프를 byte로 변경
import base64 #웹에 출력하기 위해서
import pandas as pd
import numpy as np

def graph(request):
    with open('./data/KBO_data-master/Data/rankteam.json','r',encoding='utf-8') as json_file:
        datalist = json.load(json_file)
    doosan_rank =[]
    lotte_rank =[]
    hanhwa_rank =[]
    samsung_rank =[]
    kt_rank =[]
    sk_rank =[]
    nc_rank =[]
    kiwoom_rank =[]
    kia_rank =[]
    twins_rank =[]


    for i in datalist:
        if i['팀명']=='두산':
            doosan_rank.insert(0,i['순위'])
        elif i['팀명']=='롯데':
            lotte_rank.insert(0,i['순위'])
        elif i['팀명']=='한화':
            hanhwa_rank.insert(0,i['순위'])
        elif i['팀명']=='삼성':
            samsung_rank.insert(0,i['순위'])
        elif i['팀명']=='KT':
            kt_rank.insert(0,i['순위'])
        elif i['팀명']=='SK':
            sk_rank.insert(0,i['순위'])
        elif i['팀명']=='NC':
            nc_rank.insert(0,i['순위'])            
        elif i['팀명']=='키움'or i['팀명']=='넥센':
            kiwoom_rank.insert(0,i['순위'])
        elif i['팀명']=='KIA':
            kia_rank.insert(0,i['순위'])
        elif i['팀명']=='LG':
            twins_rank.insert(0,i['순위'])

    font_name = font_manager.FontProperties(
        fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

    x = [2016,2017,2018,2019]
    # plt.figure(figsize=(12, 3))
    plt.plot(x,doosan_rank,label='두산')
    plt.plot(x,lotte_rank,label='롯데')
    plt.plot(x,hanhwa_rank,label='한화')
    plt.plot(x,samsung_rank,label='삼성')
    plt.plot(x,kt_rank,label='KT')
    plt.plot(x,sk_rank,label='SK')
    plt.plot(x,nc_rank,label='NC')
    plt.plot(x,kiwoom_rank,label='키움')
    plt.plot(x,kia_rank,label='KIA')
    plt.plot(x,twins_rank,label='LG')
    plt.yticks(np.arange(1,11,1))
    plt.gca().invert_yaxis()
    plt.xticks(np.arange(2016,2020,1))   
    plt.xlabel('연도')
    plt.ylabel('순위')
    plt.title('팀 순위 변동 그래프')
    plt.legend()
    plt.draw()
    img =io.BytesIO() #그린그래프를 바이트로 변경
    plt.savefig(img, format="png") #png포맷으로 변경
    graph_url=base64.b64encode(img.getvalue()).decode()
    plt.close() #그래프 종료
    
    return render(request, 'record/graph.html',{"graph1":'data:image/png;base64,{}'.format(graph_url)})


def highlight(request):
    if request.method =='GET':
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
        # result = results[0:5]
        # print(results)
        kbo_link=[]
        kbo_title=[]
        for video in results:
            # print(video)
            link = video.attrs['href'].replace('/watch?v=','/embed/')
            title = video.attrs['title']
            # print(link, title)
            kbo_link.append(link)
            kbo_title.append(title)
        


        return render(request, 'record/highlight.html', {'kbo_link':kbo_link, 'kbo_title': kbo_title})
