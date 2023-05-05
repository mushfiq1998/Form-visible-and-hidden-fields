from django import forms
class StudentRegistration(forms.Form):
    # Declare three visible fields
    name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.IntegerField()

    # Declare a hidden field
    key = forms.CharField(widget=forms.HiddenInput())
    