from django.shortcuts import redirect, render
from .models import DoctorInfo, Userdata ,Register
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request,method=['GET','POST']):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        user=Userdata.objects.filter(email=email)

        if user.exists():
            messages.info(request,"User is already exists")
        elif password != confirm_password:
            messages.info(request,"Passwords does not match")
        else:
            Userdata.objects.create(email=email,password=password)
            return render(request,'login.html')

    return render(request,'signup.html')

def login(request,method=['GET','POST']):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        

        user=Userdata.objects.filter(email=email)

        if user.exists():
           return redirect('/home/')
        else:    
            messages.error(request,'email and password are incorrect')
    return render(request,'login.html')

def home(request):
    doctor_info=DoctorInfo.objects.all()
    return render(request,'home.html',{'doctors':doctor_info})

def doctorappoint(request,id):
    doctor=DoctorInfo.objects.get(id=id)
    return render (request,'reg.html',{'doctor':doctor})

def register(request):
    if request.method=='POST':
        doc_n=request.POST.get('drname')
        p_name=request.POST.get('name')
        p_age=request.POST.get('age')
        p_gender=request.POST.get('gender')
        p_contact=request.POST.get('contact')
        problem=request.POST.get('prb')
        
        Register.objects.create(d_name=doc_n,p_name=p_name,p_age=p_age,p_gender=p_gender,p_contact=p_contact,problem=problem)
    return render(request,'success.html')