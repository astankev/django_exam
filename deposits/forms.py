from django import forms
from deposits.models import Deposit


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = [
            'deposit',
            'term',
            'rate',
        ]
        widgets = {
            'deposit': forms.TextInput(attrs={'class':'contact-form','placeholder': 'euro'}),
            'term': forms.TextInput(attrs={'class': 'contact-form', 'placeholder': 'years'}),
            'rate': forms.TextInput(attrs={'class': 'contact-form', 'placeholder': 'decimal'}),
                   }