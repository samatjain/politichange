from django.http import HttpResponse
from django.shortcuts import render

from mauve_duck.agile_otter.models import Participant

def index(request):
    all_users = Participant.objects.all()
    context = {
            'all_users': all_users
            }
    return render(request, 'index.html', context)

def registration(request):
	"""Registration page template called and info saved"""
	context = {           }
	return render(request, 'constituent/index.html', context)

def start_campaign(request):
	"""Register a new campaign """
	return render(request, 'politician/index.html', {})