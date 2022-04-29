from django.urls import path

from accountapp.views import hello

urlpatterns = [
    path('hello/', hello, name='hello')
]