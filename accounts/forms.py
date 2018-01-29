from django import forms

from accounts.models import Debt


class DebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        fields = '__all__'
