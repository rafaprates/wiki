from django import forms
from . import util

class CreatePageForm(forms.Form):
   title = forms.CharField(label='Title')
   content = forms.CharField(label='', widget=forms.Textarea())

class EditPageForm(forms.Form):
   content = forms.CharField(label='', widget=forms.Textarea)

