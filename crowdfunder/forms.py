from django import forms
from django.forms import ModelForm, DateInput
from django.core import validators
from django.core.validators import MinValueValidator
import datetime as dt
from datetime import datetime
from crowdfunder.models import Project, Reward, Backing


class RewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = ('title', 'amount', 'description')


class ProjectForm(ModelForm):
    title = forms.CharField(max_length=255)
    description = forms.Textarea()
    goal = forms.IntegerField(validators=[MinValueValidator(1, message='Goal must be a positive number')])
    start_date = forms.DateField(widget=DateInput(attrs={'type': 'date', 'min': dt.date.today()}))
    end_date = forms.DateField(widget=DateInput(attrs={'type': 'date', 'min': dt.date.today()}))

    class Meta:
        model = Project
        fields = ['title', 'description', 'goal', 'start_date', 'end_date']

    def clean(self):
        goal = self.cleaned_data.get('goal')
    
