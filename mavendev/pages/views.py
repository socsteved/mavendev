from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class CXPageView(TemplateView):
    template_name = 'cx.html'

class DQPageView(TemplateView):
    template_name = 'dq.html'

class SendPageView(TemplateView):
    template_name = 'send.html'

class IndustryPageView(TemplateView):
    template_name = 'indsol.html'

class HXPageView(TemplateView):
    template_name = 'hx.html'
