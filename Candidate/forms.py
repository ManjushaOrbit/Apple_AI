from django import forms
from .models import CandidateData,  BusinessCard, KYC, Patient, Adhar

class CandidateDataForm(forms.ModelForm):
    class Meta:
        model = CandidateData
        fields = '__all__' 


class KYCDataForm(forms.ModelForm):
    class Meta:
        model = KYC
        fields = '__all__'

class AdharDataForm(forms.ModelForm):
    class Meta:
        model = Adhar
        fields = '__all__'

class PatientDataForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class BusinessCardDataForm(forms.ModelForm):
    class Meta:
        model = BusinessCard
        fields = '__all__'