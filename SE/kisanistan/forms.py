from django import forms


class usercrops(forms.Form):
    name = forms.CharField(max_length=60)
    emailaddress = forms.CharField(max_length=60)
    season = forms.CharField(max_length=60)
    price = forms.CharField(max_length=60)
