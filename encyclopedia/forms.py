from django import forms

class CreatePageForm(forms.Form):
   title = forms.CharField(label='title')
   content = forms.CharField(label='', widget=forms.Textarea())

class EditPageForm(forms.Form):
   content = forms.CharField(widget=forms.Textarea)

