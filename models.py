from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique= True)
    password = models.CharField(max_length = 20)

class Add_Emoployess(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50) 
    email = models.EmailField(unique= True)
    password = models.CharField(max_length = 20)
    employee_id = models.CharField(max_length=50)
    joining_date = models.CharField(max_length=50)
    phone = models.CharField(max_length = 10)
    department = models.CharField(max_length = 100)
    designation = models.CharField(max_length = 100)
    profile_pic=models.FileField(upload_to='hrms/img/',default='avatar.png')
    otp = models.IntegerField(default = 459)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)

    # after update profile

    address = models.CharField(max_length= 500, blank = True)
    birthdate = models.CharField(max_length=50)
    gender = models.CharField(max_length= 10)
    passport_number = models.CharField(max_length= 50)
    passport_ex_date = models.CharField(max_length= 50)
    nationality = models.CharField(max_length= 50)
    religion = models.CharField(max_length= 50)
    marital_status = models.CharField(max_length= 10)
    child = models.IntegerField(max_length=50)
    bank_name = models.CharField(max_length= 50)
    acc_no = models.IntegerField(max_length=50)
    ifsc_code = models.CharField(max_length= 50)
    pan_no = models.CharField(max_length= 50)
    pincode = models.CharField(max_length= 50)
    country = models.CharField(max_length= 50)
    state = models.CharField(max_length= 50)


