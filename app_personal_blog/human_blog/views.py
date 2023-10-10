#
#
#
#
#
from django.views.generic import TemplateView
#
from django.shortcuts import redirect
#
from .forms import MesajForm


class HomePageView(TemplateView):
    template_name = 'human_blog/blog_list.html'


class AboutPageView(TemplateView):
    template_name = 'human_blog/about.html'


class CVResumePageView(TemplateView):
    template_name = 'human_blog/resume.html'


class ContactPageView(TemplateView):
    template_name = 'human_blog/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MesajForm()
        return context

    def post(self, request, *args, **kwargs):
        form = MesajForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('succes')
        return self.render_to_response(self.get_context_data(form=form))


# View for succes
class SuccesPageContact(TemplateView):
    template_name = 'human_blog/succes_contact.html'


class InterviuriPageView(TemplateView):
    template_name = 'human_blog/interviuri.html'


# View for blog_post
# And for get in touch ---> Make a contact page!
