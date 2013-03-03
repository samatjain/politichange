from django.http import HttpResponse
from django.shortcuts import render

from mauve_duck.agile_otter.models import Participant

# from mauve_duck.agile_otter import CampaignForm

def index(request):
    all_users = Participant.objects.all()
    context = {
            'all_users': all_users
            }
    return render(request, 'index.html', context)

def registration(request):
	"""Registration page template called and info saved"""
	context = {           }
	return render(request, 'campaign/index.html', context)

def start_campaign(request):
	"""Register a new campaign """
	from django.shortcuts import render
	from django.http import HttpResponseRedirect

	def contact(request):
	    if request.method == 'POST': # If the form has been submitted...
	        form = CampaignForm(request.POST) # A form bound to the POST data
	        if form.is_valid(): # All validation rules pass
	            # Process the data in form.cleaned_data
	            # ...
	            return HttpResponseRedirect('/thanks/') # Redirect after POST
	    else:
	        form = CampaignForm() # An unbound form

	    return render(request, 'politician/campaign.html', {
	        'form': form,
	    })
	return render(request, 'politician/create-campaign.html', {})
	
def politician_start(request):
	"""page for politician action initiation """
	return render(request, 'politician/index.html', {})
	
def campaign(request):
	if	request.method == 'POST':
		form = CampaignForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/')
	else:
		form = CampaignForm()
		
	return render(request, 'campaign.html',{
		form : form,
	})