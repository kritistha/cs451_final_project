from django.shortcuts import render
from django.urls import reverse_lazy

from geopy import Nominatim
from geopy import distance

from django.views import generic 
from django.conf import settings 
from .models import Job


APP_LOCATION = settings.DEFAULT_LOCATION

class HomeView(generic.TemplateView):
	template_name = 'home.html'


class JobView(generic.DetailView):
	model = Job
	template_name = 'job.html'
	

class JobListView(generic.ListView):
	model = Job
	template_name = 'job_list.html'
	
class JobSearchView(generic.ListView):
	model = Job
	template_name = 'job_search.html'
	
	def get_context_data(self, **kwargs):
		context = super(JobSearchView, self).get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()
        return context
