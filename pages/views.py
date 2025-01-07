"""nnn"""
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """home"""
    template_name = 'home.html'
