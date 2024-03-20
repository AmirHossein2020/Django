from django.shortcuts import render
from django.views.generic import TemplateView , ListView, CreateView
from .models import Resume , Project
from .forms import Formresume , Formproject
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class ResumeView(ListView):
    model = Resume
    template_name = 'Resume.html'

class ProjectView(ListView):
    model = Project
    template_name = 'Project.html'

class Newresume(CreateView):
    model = Resume
    template_name = 'new_resume.html'
    form_class = Formresume
    success_url = reverse_lazy('home')

class Newproject(CreateView):
    model = Project
    template_name = 'new_project.html'
    form_class = Formproject
    success_url = reverse_lazy('home')