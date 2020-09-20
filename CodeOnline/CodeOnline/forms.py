from django import forms

class CodeInput(forms.Form):
    codearea = forms.CharField(widget=forms.Textarea(), label="")