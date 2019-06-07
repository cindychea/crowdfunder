from django import forms
from django.forms import ModelForm, DateInput
from django.core import validators
from django.core.validators import MinValueValidator
import datetime as dt
from datetime import datetime, timedelta
from crowdfunder.models import Project, Reward, Backing
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = ('title', 'amount', 'description')


class ProjectForm(ModelForm):
    title = forms.CharField(max_length=255)
    description = forms.Textarea()
    goal = forms.IntegerField(validators=[MinValueValidator(1, message='Goal must be a positive number')])
    start_date = forms.DateField(widget=DateInput(attrs={'type': 'date', 'min': dt.date.today()}))
    end_date = forms.DateField(widget=DateInput(attrs={'type': 'date', 'min': (dt.date.today() + dt.timedelta(days=1))}))

    class Meta:
        model = Project
        fields = ['title', 'description', 'goal', 'start_date', 'end_date']

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')