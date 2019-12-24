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

    # Personal Profile
    birthdate = models.CharField(max_length=50)
    gender = models.CharField(max_length= 10)
    address = models.CharField(max_length= 500, blank = True)
    state = models.CharField(max_length= 50)
    country = models.CharField(max_length= 50)
    pincode = models.CharField(max_length= 50)

    # Details
    passport_number = models.CharField(max_length= 50)
    passport_ex_date = models.CharField(max_length= 50)
    nationality = models.CharField(max_length= 50)
    religion = models.CharField(max_length= 50)
    marital_status = models.CharField(max_length= 10)
    child = models.IntegerField(max_length=50)


    # bank_name = models.CharField(max_length= 50)
    # acc_no = models.IntegerField(max_length=20)
    # ifsc_code = models.CharField(max_length= 50)
    # pan_no = models.CharField(max_length= 50)

    # family Information
    name = models.CharField(max_length= 50)
    relationship = models.CharField(max_length= 50)
    dob = models.CharField(max_length= 50)
    mobile = models.CharField(max_length= 50)

    # Education Information
    institute = models.CharField(max_length= 500)
    subject = models.CharField(max_length= 500)
    startind_date = models.CharField(max_length= 50)
    complete_date = models.CharField(max_length= 50)
    degree = models.CharField(max_length= 50)
    grade = models.CharField(max_length= 50)

    # Experience Information
    c_name = models.CharField(max_length= 500)
    location = models.CharField(max_length= 50)
    position = models.CharField(max_length= 50)
    p_from = models.CharField(max_length= 50)
    p_to = models.CharField(max_length= 50)

class Ticket(models.Model):
    uid = models.ForeignKey(Add_Emoployess,on_delete = models.CASCADE)
    subject = models.CharField(max_length= 50)
    ticket_id = models.CharField(max_length= 50)
    assign_staff = models.CharField(max_length= 50)
    client = models.CharField(max_length= 50)
    priority = models.CharField(max_length= 50)
    cc = models.CharField(max_length= 50)
    assign = models.CharField(max_length= 50)
    followers = models.CharField(max_length= 50)
    description = models.CharField(max_length= 50)
    file=models.FileField(upload_to='img/')
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)



