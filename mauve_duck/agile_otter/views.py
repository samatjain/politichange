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
	return render(request, 'registration.html', context)
