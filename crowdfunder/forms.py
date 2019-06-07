from django import forms
from crowdfunder.models import Project, Reward, Backing

class RewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = ('title', 'amount', 'description')