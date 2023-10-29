from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models import*
from django.shortcuts import render, redirect



# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def loginAction(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(Username=username,Password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,"Invalid Username or Password")
    return render(request,'click.html')



def register(request):
    return render(request,'register.html')

def registerAction(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        new=register_tb.objects.filter(Username=username,Password=password,confirmpassword=confirmpassword)
        messages.add_message(request, messages.INFO, "Registeration succesfully")
    return redirect('login')

# def loginpage(request):
#     return render(request,'loginpage.html')
# def loginpageAction(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(Username=username,Password=password)
#     return render(request,"click.html")

def form(request):
    return render(request,'form.html')

def formAction(request):
    if request.method=='POST':
        name=request.POST['name']
        dob=request.POST['dob']
        age=request.POST['age']
        gender=request.POST['gender']
        phonenumber=request.POST['phoneno']
        email=request.POST['email']
        address=request.POST['address']
        department=request.POST['department']
        courses=request.POST['courses']
        materials=request.POST['materials']
        form=form_tb(Name=name,Dob=dob,Age=age,Gender=gender,Phonenumber=phonenumber,Email=email,Address=address,Department=department,Courses=courses,Materials=materials)
        form.save()
        messages.add_message(request,messages.INFO,"Order Confirmed")
    return redirect('form')

def logout(request):
    return redirect('index')


