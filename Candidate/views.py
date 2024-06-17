from django.shortcuts import render, redirect
from .models import CandidateData, Patient, BusinessCard, KYC, Adhar
from django.views.decorators.csrf import csrf_exempt
from .forms import CandidateDataForm,KYCDataForm, AdharDataForm, PatientDataForm,BusinessCardDataForm
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
# Create your views here.

@csrf_exempt
def createCandidateData(request):
    if request.method == "POST":
        form = CandidateDataForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
            print("save data")
            return redirect('get_cadiadate')  # Redirect to success page after successful form submission
        else:
            print(form.errors)
    else:
        form = CandidateDataForm()
        print("not valid")
    return render(request, 'get_candidate.html',{'form': form})

@csrf_exempt
def submit_buisnesscard_data(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        print(data["first_name"])
        buisnesscard = BusinessCard.objects.create(first_name=data["first_name"],last_name=data["last_name"],phone=data["phone"], email=data['email'])
        return JsonResponse({"status":True,"mesaage":"Data saved successfully",'data':model_to_dict(buisnesscard)})
    else:
        return JsonResponse({"status":False,"mesaage":"Invalid Data"})

@csrf_exempt
def create_patient(request):
    if request.method == 'POST':
        print("dd",json.loads(request.body.decode()))
        data = json.loads(request.body.decode())
        patient = Patient(firstname=data["firstname"],lastname=data["lastname"],phone=data["phone"], address=data['address'], dob = data['dob'], age = data['age'],sex = data['sex'], insurance_number=data['insurance_number'],insurance_holder_name=data['insurance_holder_name'])
        patient.save()
        return JsonResponse({"status":True,"mesaage":"Data saved successfully"})    
    else:
        return JsonResponse({"status":False,"mesaage":"Invalid Data"})

@csrf_exempt
def submit_adhar_data(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        adhar = Adhar(name=data["name"],year_of_birth=data["year_of_birth"],gender=data["gender"], aadharno=data['aadharno'],fathers_name = data['fathers_name'])
        adhar.save()
        return JsonResponse({"status":True,"mesaage":"Data saved successfully"})    
    else:
        return JsonResponse({"status":False,"mesaage":"Invalid Data"})

@csrf_exempt
def submit_kyc_data(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        kyc = KYC(name=data["name"],dob=data["dob"],gender=data["gender"], aadharno=data['aadharno'],fathers_name = data['fathers_name'], address= data['address'],marital_status=data['marital_status'] ,nationality=data['nationality'],pan_number=data['pan_number'],residence_details=data['residence_details'],status=['status'])
        kyc.save()
        return JsonResponse({"status":True,"mesaage":"Data saved successfully"})
    else:
        return JsonResponse({"status":False,"mesaage":"Invalid Data"})

@login_required(login_url = "login")
def get_all_data(request):
    patient_data = list(Patient.objects.all().values())
    buisnesscard = list(BusinessCard.objects.all().values())
    kycdata = list(KYC.objects.all().values())
    adhar = list(Adhar.objects.all().values())

    data = {
            "patient_data" : patient_data,
            "buisnesscard" : buisnesscard,
            "kycdata" : kycdata,
            "adhar"  : adhar,
    }
    # return JsonResponse({"status":True,"mesaage":"found data", "data":data})
    return render(request,"all_data.html",{"data":data})






