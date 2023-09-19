#
#
#
#
#
from django.urls import path
from . import views


urlpatterns = [
    path('', views.hi_world_view, name="robot-home"),
]
