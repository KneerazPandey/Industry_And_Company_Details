from django import forms
from . models import IndustryType, CompanyDetails


class IndustryTypeCreationForm(forms.ModelForm):
    class Meta:
        model = IndustryType
        fields = '__all__'


class CompanyDetailsCreationForm(forms.ModelForm):
    class Meta:
        model = CompanyDetails
        fields = '__all__'