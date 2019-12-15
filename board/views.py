from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from base64 import b64encode
from .models import Board
from django.db.models import Max, Min
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'board/index.html')

def boardList(request):
    if request.method == "GET":
        request.session['brdhit'] = 1

        searchType = request.GET.get('searchType', 'brd_title')
        searchKeyword = request.GET.get('searchKeyword', '')
        
        if searchType == "brd_title":
            board = Board.objects.filter(brd_title__icontains = searchKeyword).order_by('-brd_no')
        elif searchType == "brd_content":
            board = Board.objects.filter(brd_content__icontains = searchKeyword).order_by('-brd_no')
        elif searchType == "brd_writer":
            board = Board.objects.filter(brd_writer__icontains = searchKeyword).order_by('-brd_no')

        paginator = Paginator(board, 10)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        
        pageList = []
        
        for i in range(1, paginator.num_pages + 1, 1):
            pageList.append(i)

        return render(request, 'board/boardList.html', {'board': board, 'posts': posts, 'pageList': pageList, 'searchType': searchType, 'searchKeyword': searchKeyword})

def detail(request):
    no = request.GET.get("no", 0)

    # 조회수 증가(session당 1개로 제한)
    if 'brdHit' in request.session:
        if request.session['brdhit'] == 1:
            board = Board.objects.get(brd_no = no)
            board.brd_hit = board.brd_hit + 1
            board.save()
            
            request.session['brdhit'] = 0

    # 상세 글내용 불러오기
    board = Board.objects.get(brd_no = no)

    # 이전글 번호 찾기
    preNo = Board.objects.filter(brd_no__lt = no).aggregate(brd_no = Max('brd_no'))

    # 다음글 번호 찾기
    nextNo = Board.objects.filter(brd_no__gt = no).aggregate(brd_no = Min('brd_no'))

    return render(request, 'board/detail.html', {'board': board, 'preNo': preNo, 'nextNo': nextNo})

@csrf_exempt
def write(request):
    if request.method == "GET":
        return render(request, 'board/write.html')

    elif request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        writer = request.session['userName']

        board = Board(brd_title = title, brd_content = content, brd_writer = writer, brd_hit = 0)
        board.save()

        return redirect('/board/boardList')

@csrf_exempt
def update(request):
    if request.method == "GET":
        no = request.GET.get('no', 0)

        board = Board.objects.get(brd_no = no)

        return render(request, 'board/update.html', {'board': board})

    elif request.method == "POST":
        no = request.POST['no']
        title = request.POST['title']
        content = request.POST['content']

        board = Board.objects.get(brd_no = no)
        board.brd_title = title
        board.brd_content = content
        board.save()

        return redirect('/board/detail?no=' + no)

def delete(request):
    no = request.GET.get('no', 0)

    Board.objects.get(brd_no = no).delete()

    return redirect('/board/boardList')