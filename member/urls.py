from django.urls import path
from . import views

urlpatterns = [
    path('join', views.join, name='join'),
    path('memberList', views.memberList, name='memberList'),
    path('login', views.login, name='login'),
    path('idCheck', views.idCheck, name='idCheck'),
    path('logout', views.logout, name='logout'),
    path('updateInfo', views.updateInfo, name='updateInfo'),
    path('updatePW', views.updatePW, name='updatePW'),
    path('delete', views.delete, name='delete'),
]