from django import forms
from . import util

class CreatePageForm(forms.Form):
   title = forms.CharField(label='title')
   content = forms.CharField(label='', widget=forms.Textarea())

class EditPageForm(forms.Form):

   
   #markdown = util.get_entry("title")
   content = forms.CharField(widget=forms.Textarea)

