from django.shortcuts import render
from django.views.generic import TemplateView

class HomepageView(TemplateView):
      template_name = 'home.html'

class AboutpageView(TemplateView):
      template_name = 'about.html'

class ContactpageView(TemplateView):
      template_name = 'contact.html'


class ServicespageView(TemplateView):
      template_name = 'services.html'