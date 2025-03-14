from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['category', 'description', 'location']

class SimpleAuthForm(forms.Form):
    email = forms.EmailField(label="Adresse e-mail", max_length=254)
    name = forms.CharField(label="Nom", max_length=150)
