from django.contrib import admin
from .models import CandidateData, BusinessCard, KYC, Patient, Adhar

# Register your models here.
admin.site.register(CandidateData)
admin.site.register(BusinessCard)
admin.site.register(KYC)
admin.site.register(Patient)
admin.site.register(Adhar)