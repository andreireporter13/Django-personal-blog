#
#
#
#
#
from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('despre-mine/', views.AboutPageView.as_view(), name="about"),
    path('cv-resume/', views.CVResumePageView.as_view(), name="cv-resume"),
    path('contact/', views.ContactPageView.as_view(), name="contact"),
    path('interviuri/', views.InterviuriPageView.as_view(), name="interviuri"),

    # succes contact page
    path('mesaj-trimis-cu-succes/', views.SuccesPageContact.as_view(), name="succes"),
]
