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


# View for blog_post
# And for get in touch ---> Make a contact page!
