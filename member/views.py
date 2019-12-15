from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.paginator import Paginator
import json
from .models import Member

# Create your views here.
def memberList(request):
    member = Member.objects.all()

    paginator = Paginator(member, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    pageList = []
    
    for i in range(1, paginator.num_pages + 1, 1):
        pageList.append(i)

    return render(request, 'member/memberList.html', {'member': member, 'posts': posts, 'pageList': pageList})

@csrf_exempt
def join(request):
    if request.method == "GET":
        return render(request, 'member/join.html')

    elif request.method == "POST":
        id = request.POST['id']
        pw = request.POST['pw']
        name = request.POST['name']
        tel = request.POST['tel']
        email = request.POST['email']

        member = Member(mem_id = id, mem_pw = pw, mem_name = name, mem_tel = tel, mem_email = email)
        member.save()

        context = {'join_status': 1}

        return HttpResponse(json.dumps(context), content_type='application/json')

@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, 'member/login.html')

    elif request.method == "POST":
        id = request.POST['id']
        pw = request.POST['pw']

        member = Member.objects.get(mem_id = id, mem_pw = pw)
        request.session['userId'] = member.mem_id
        request.session['userName'] = member.mem_name
        request.session['brdHit'] = 1

        context = {'username': member.mem_name}

        return HttpResponse(json.dumps(context), content_type='application/json')
            
def logout(request):
    del request.session['userId']
    del request.session['userName']

    return redirect('/index')

@csrf_exempt
def updateInfo(request):
    if request.method == "GET":
        id = request.session['userId']

        member = Member.objects.get(mem_id = id)

        return render(request, 'member/updateInfo.html', {'member': member})
    
    elif request.method == "POST":
        id = request.session['userId']
        name = request.POST['name']
        tel = request.POST['tel']
        email = request.POST['email']     

        member = Member.objects.get(mem_id = id)
        member.mem_name = name
        member.mem_tel = tel
        member.mem_email = email
        member.save()

        del request.session['userName']
        request.session['userName'] = name

        context = {'update_status': 1}

        return HttpResponse(json.dumps(context), content_type='application/json')

@csrf_exempt
def updatePW(request):
    if request.method == "GET":
        return render(request, 'member/updatePW.html')
    
    elif request.method == "POST":
        id = request.session['userId']
        pw = request.POST['pw']
        re_pw = request.POST['re_pw']

        member = Member.objects.get(mem_id = id, mem_pw = pw)

        member.mem_pw = re_pw
        member.save()
        
        del request.session['userId']

        context = {'update_status': 1}

        return HttpResponse(json.dumps(context), content_type='application/json')

@csrf_exempt
def delete(request):
    if request.method == "GET":
        return render(request, 'member/delete.html')

    elif request.method == "POST":
        id = request.session['userId']
        pwCheck = request.POST['pw']

        member = Member.objects.get(mem_id = id, mem_pw = pwCheck)

        if member is not None:
            Member.objects.get(mem_id = id).delete()

            del request.session['userId']
            del request.session['userName']

        context = {'delete_status': 1}

        return HttpResponse(json.dumps(context), content_type='application/json')