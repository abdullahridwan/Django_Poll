from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),

    #path('vader', views.vader, name='vader')
]
