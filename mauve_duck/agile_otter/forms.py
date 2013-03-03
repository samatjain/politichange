from django.forms import ModelForm

class CampaignForm(ModelForm):
	class Meta:
		model = Campaign