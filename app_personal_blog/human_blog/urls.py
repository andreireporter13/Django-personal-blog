#
#
#
#
#
from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('oamenii-din-blog/', views.HomePageView.as_view(), name="home"),
    path('despre-mine', views.AboutPageView.as_view(), name="about"),
]
