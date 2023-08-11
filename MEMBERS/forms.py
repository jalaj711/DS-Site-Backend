from django.forms import ModelForm
from django import forms
from .models import *

class MemberCreationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'