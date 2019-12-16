from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .models import Record
from .models import Pitcher
from .models import Team
from .models import Hitter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib.request, time


# Create your views here.
def recordList(request):
    if request.method == "GET":
        # json 파일 내용 DB 에 insert
        # dataList = []

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
        # datalist =[]

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
        # datalist=[]

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

def teamyear(request):
    if request.method =='GET':
        # json 파일 내용 db에 insert
        # datalist = []

        # for data in datalist:
        #     t_no   = data['순위']
        #     t_name = data['팀명']
        #     t_game = data['경기']
        #     t_win  = data['승']
        #     t_lose = data['패']
        #     t_draw = data['무']
        #     t_per  = data['승률']
        #     t_chai = data['게임차']
        #     t_10   = data['최근10경기']
        #     t_cont = data['연속']
        #     t_home = data['홈']
        #     t_away = data['방문']
        #     t_year = data['연도']
            
        #     teamyear = Team(t_no=t_no,t_name=t_name,t_game=t_game,t_win=t_win,t_lose=t_lose,t_draw=t_draw,t_per=t_per,t_chai=t_chai,t_10=t_10,t_cont=t_cont,t_home=t_home,t_away=t_away,t_year=t_year )
        #     teamyear.save()

        search_year = request.GET.get('search_year','2019')

        if search_year != "":
            teamList = Team.objects.filter(t_year=search_year).order_by('t_no')
        
        else:
            teamList = Team.objects.filter(t_year='2019').order_by('t_no')
            search_year = 2019

        return render(request, 'record/teamyear.html',{'teamList':teamList, 't_year':search_year})


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
