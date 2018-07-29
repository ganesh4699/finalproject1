from django import forms

class FormName(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField(max_length=50)
    text=forms.CharField(widget=forms.Textarea)