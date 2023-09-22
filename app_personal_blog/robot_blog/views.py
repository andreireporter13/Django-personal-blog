#
#
#
#
#
from django.views.generic import TemplateView


class RobotPageView(TemplateView):
    template_name = 'human_blog/ask_robot.html'
