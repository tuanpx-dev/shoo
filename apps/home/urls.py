from django.urls import path

from apps.home import views

urlpatterns = [
    # ex: /polls/
    path('', views.home, name='home')
]
