from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # path('',createCandidateData, name = 'createCandidateData'),
    path('submitbuisnesscard/',submit_buisnesscard_data,name='buisnesscard'),
    path('createpatient/',create_patient,name='patient'),
    path('submitadhar/',submit_adhar_data,name='adhar'),
    path('submitkyc/',submit_kyc_data,name='kyc'),
    path('all_data/',get_all_data,name='all_data'),
]