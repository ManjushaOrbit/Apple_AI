from django.db import models

# Create your models here.


class CandidateData(models.Model):
    name = models.CharField(max_length = 500,null = False)
    post_applied = models.CharField(max_length=100,null=False)
    total_month_experinec = models.CharField(max_length = 200, null=True,blank = True)
    total_year_experinec = models.PositiveIntegerField(null= True)
    current_ctc = models.PositiveIntegerField(null = True)
    expected_ctc = models.PositiveIntegerField(null = True)

    MALE = 'M' 
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    ONE_MONTH = '1M'
    TWO_MONTHS = '2M'
    THREE_MONTHS = '3M'

    NOTICE_PERIOD_CHOICES = [
        (ONE_MONTH, '1 month'),
        (TWO_MONTHS, '2 months'),
        (THREE_MONTHS, '3 months'),
    ]
    experinece_in_sales_and_services = models.TextField(null=True)
    notice_period = models.CharField(max_length=10, choices=NOTICE_PERIOD_CHOICES, default='0M')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    reason_for_this_job = models.TextField( null=True)
    resumefile = models.FileField(upload_to = "resumes/", null= False, blank=False)
    reffered_by = models.CharField(max_length = 500, null=True)


class BusinessCard(models.Model):
    first_name = models.CharField(max_length = 100, null = True, blank= True)
    last_name = models.CharField(max_length=100, null = True,blank=True)
    phone = models.CharField(max_length=100, null=True,blank=True)
    email = models.EmailField(max_length=200, null=True,blank=True)
    

class Patient(models.Model):
    firstname = models.CharField(max_length = 100, null = True, blank= True)
    lastname = models.CharField(max_length = 100, null = True, blank= True)
    phone = models.CharField(max_length=100, null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    dob = models.CharField(max_length=20, null= True, blank =True)
    age = models.CharField(max_length=5, null=True, blank=True)
    sex = models.CharField(max_length = 10,null=True, blank=True)
    insurance_number = models.CharField(max_length=50,null=True,blank=True)
    insurance_holder_name = models.CharField(max_length=200, null=True,blank=True)

class Adhar(models.Model):
    name = models.CharField(max_length = 500,null = True,blank=True)
    year_of_birth = models.CharField(max_length = 10, null = True,blank=True)
    gender = models.CharField(max_length=10,null=True,blank=True)
    aadharno = models.CharField(max_length=20, null=True,blank=True)
    fathers_name = models.CharField(max_length = 500,null = True,blank=True)
    address = models.TextField(null=True,blank=True)

class KYC(models.Model):
    name = models.CharField(max_length = 500,null = True,blank=True)
    dob = models.CharField(max_length = 20, null = True,blank=True)
    gender = models.CharField(max_length=10,blank=True, null=True)
    aadharno = models.CharField(max_length=20, null=True,blank=True)
    fathers_name = models.CharField(max_length = 500,null = True,blank=True)
    address = models.TextField(null=True,blank=True)
    marital_status = models.CharField(max_length=10, null=True, blank= True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    pan_number = models.CharField(max_length=20, null=True,blank=True)
    residence_details = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=1000,null=True,blank=True)






