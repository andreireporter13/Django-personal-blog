#
#
#
#
#
from django.views.generic import TemplateView


class RobotPageView(TemplateView):
    template_name = 'robot_blog/ask_robot.html'
