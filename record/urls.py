from django.urls import path
from . import views

urlpatterns = [
    path('recordList', views.recordList, name='recordList'),
    path('pitcherList', views.pitcherList, name='pitcherList'),
    path('hitterList', views.hitterList, name='hitterList'),
    path('teamyear', views.teamyear, name='teamyear'),
<<<<<<< HEAD
    path('graph', views.graph, name='graph')
=======
    path('highlight', views.highlight, name='highlight')

>>>>>>> 91dcc8f34e6c2d1c48f1315063b4d7e53f286096
]