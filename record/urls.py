from django.urls import path
from . import views

urlpatterns = [
    path('recordList', views.recordList, name='recordList'),
    path('pitcherList', views.pitcherList, name='pitcherList'),
    path('hitterList', views.hitterList, name='hitterList'),
    path('teamyear', views.teamyear, name='teamyear'),
    path('graph', views.graph, name='graph'),
    path('highlight', views.highlight, name='highlight')

]