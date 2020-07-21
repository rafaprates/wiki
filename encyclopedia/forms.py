from django import forms

class CreatePageForm(forms.Form):
   title = forms.CharField(label='title')
   content = forms.CharField(label='', widget=forms.Textarea())