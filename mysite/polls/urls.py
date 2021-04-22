from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('news', views.test, name="test")
    #path('vader', views.vader, name='vader')
]
