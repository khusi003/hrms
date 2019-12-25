from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
# Create your views here.
def indexpage(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request,'hrms/index.html',{'uid':uid})
    else:
        return render(request,'hrms/login.html')

def login(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request,'hrms/index.html')
    else:
        return render(request,'hrms/login.html')

def login_hr(request):
    try:
        if 'email' in request.session:
            uid=User.objects.get(email=request.session['email'])
            return render(request,'hrms/index.html')
        else:
            email = request.POST['email']
            password = request.POST['password']
            uid = User.objects.get(email=email)
            if uid:
                if uid.password == password:
                    request.session['uid']=uid.id
                    request.session['email']=uid.email
                    return render(request,'hrms/index.html')
                else:
                    e_msg = "password is wrong"    
                    return render(request,'hrms/login.html',{'e_msg':e_msg})
            else:
                e_msg="You do not have authority to access this page" 
                return render(request,'hrms/login.html',{'e_msg':e_msg})       
    except: 
        e_msg="User Does Not Exist"   
        return render(request,'hrms/login.html',{'e_msg':e_msg})  


def profile(request):
    try:
        data = Add_Emoployess.objects.all()
        if data:
            for i in data:
                print('===============',i.id)
                return render(request,'hrms/profile.html',{'data':data}) 
        else:
            return render(request,'hrms/profile.html') 
    except:
        return render(request,'hrms/profile.html')

def employees(request):
    try:
        data = Add_Emoployess.objects.all()
        if data:
            for i in data:
                print('===============',i.id)
                return render(request,'hrms/employees.html',{'data':data}) 
        else:
            return render(request,'hrms/employees.html') 
    except:
        return render(request,'hrms/employees.html') 



def add_employee(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']
    employee_id = request.POST['employee_id']
    joining_date = request.POST['joining_date']
    phone = request.POST['phone']
    department = request.POST['department']
    designation = request.POST['designation']
    # print('=======================',firstname)
    # print('=============================',lastname)
    # print('=============================',email)
    # print('===============================',password)
    # print('===========================',repassword)
    # print('========================',employee_id)
    # print('=============================',joining_date)
    # print('=====================',phone)
    # print('==============================',department)
    # print('================',designation)
    if password==repassword:
        uid = Add_Emoployess.objects.create(firstname=firstname,lastname=lastname,email=email,password=password,employee_id=employee_id,joining_date=joining_date,phone=phone,department=department,designation=designation)
        if uid:
            s_msg="Successfully Added"
            send_mail('Welcome to HRMS system','your login id and password are : '+email +password,'khushipatel284@gmail.com',[email])
            return render(request,'hrms/employees.html',{'s_msg':s_msg})
        else:
            e_msg="Try Again"
            return render(request,'hrms/employees.html',{'e_msg':e_msg})
    else:
        e_msg='password and confirm password does not match'
        return render(request,'hrms/employees.html',{'e_msg':e_msg})



def ticket(request):
    return render(request,'hrms/tickets.html')  

def holiday(request):
    try:
        data = Holidays.objects.all()
        if data:
            for i in data:
                return render(request,'hrms/holidays.html',{'data':data}) 
        else:        
            return render(request,'hrms/holidays.html') 
    except:
        return render(request,'hrms/holidays.html')  


def add_holiday(request):
    name = request.POST['name']
    date = request.POST['date']
    day = request.POST['day']
    uid = Holidays.objects.create(name=name,date=date,day=day)
    if uid:
        # print('=============================success') 
        return render(request,'hrms/holidays.html')
    else:
        return render(request,'hrms/holidays.html')  

def department(request):
    try:
        data = Department.objects.all()
        if data:
            # for i in data:
            return render(request,'hrms/departments.html',{'data':data}) 
        else:
            return render(request,'hrms/departments.html') 
    except:
        return render(request,'hrms/departments.html') 


def add_department(request):
    try:
        data = Department.objects.all()
        d_name = request.POST['d_name']
        uid=Department.objects.create(d_name=d_name)
        if uid:
            return render(request,'hrms/departments.html',{'data':data})  
        else:
            return render(request,'hrms/departments.html')  
    except:
            return render(request,'hrms/departments.html')


def designation(request):
    try:
        data = Designation.objects.all().prefetch_related('d_name')
        if data:
            # for i in data:
            return render(request,'hrms/designations.html',{'data':data}) 
        else:
            return render(request,'hrms/designations.html') 
    except:
        return render(request,'hrms/designations.html') 


def add_designation(request):
    try:
        data = Designation.objects.all().prefetch_related('d_name')
        d_name = request.POST['d_name']
        uid = Department.objects.get(d_name=d_name)
        if uid:
            print('==============',uid)
        
            designation_name = request.POST['designation_name']
            print('====================',designation_name)
            
            insert=Designation.objects.create(designation_name=designation_name,d_name=uid)
            if insert:
                print('===================success')
                return render(request,'hrms/designations.html',{'data':data})  
            else:
                return render(request,'hrms/designations.html')  
    except:
            return render(request,'hrms/designations.html')              
        

def logout(request):
    if "email" in request.session:
        del request.session['uid']
        del request.session['email']
        return render(request,'hrms/login.html')
    else:
        return render(request,'hrms/login.html')   
    
    