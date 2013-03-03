from django.forms  import ModelForm
from mauve_duck.agile_otter.models import Campaign

class CampaignForm(ModelForm):
	class Meta:
		model = Campaign