from django.urls import path
from . import views

urlpatterns = [
    path('boardList', views.boardList, name='boardList'),
    path('write', views.write, name='write'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),
    path('detail', views.detail, name='detail'),
]