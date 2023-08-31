from django import forms
from django.contrib.auth.models import User

class BalanceTransferForm(forms.Form):
    receiver = forms.ModelChoiceField(queryset=User.objects.all())
    amount = forms.DecimalField(max_digits=10, decimal_places=2)