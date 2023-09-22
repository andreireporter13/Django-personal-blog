#
#
#
#
#
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'human_blog/blog_list.html'


class AboutPageView(TemplateView):
    template_name = 'human_blog/about.html'


class CVResumePageView(TemplateView):
    template_name = 'human_blog/resume.html'


class ContactPageView(TemplateView):
    template_name = 'human_blog/contact.html'


class RobotPageView(TemplateView):
    template_name = 'human_blog/ask_robot.html'


class InterviuriPageView(TemplateView):
    template_name = 'human_blog/interviuri.html'


# View for blog_post
# And for get in touch ---> Make a contact page!
