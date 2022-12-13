from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.
def landing(request):
    return render(request, 'core/landing.html')


# class DashboardView(LoginRequiredMixin, TemplateView):
#     """dashboard"""
#     template_name = 'dashboard.html'
#

#
# class LandingView(TemplateView):
#     """landing"""
#     template_name = 'landing.html'

