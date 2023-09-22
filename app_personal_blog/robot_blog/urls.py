#
#
#
#
#
from django.urls import path
from . import views


urlpatterns = [
    path('scrie-i-botului/', views.RobotPageView.as_view(), name="robot"),
]
