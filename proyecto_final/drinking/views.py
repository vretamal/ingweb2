from django.shortcuts import render, render_to_response
from django.views import generic
from django.template.context import RequestContext


class HomeView(generic.TemplateView):
    template_name = "drinking/home.html"