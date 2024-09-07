from django import forms

class QuoteSearchForm(forms.Form):
    author = forms.CharField(max_length=100, required=False)
