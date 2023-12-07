from django.shortcuts import render,redirect
from SiteAdmin.models import*
from Parent.models import*
from Teacher.models import*
from django.contrib import messages
def index(request):
    return render(request,'index.html')
# Create your views here.
def login(request):
    return render(request,'login.html')
def loginAction(request):
    Username=request.POST['username']
    Password=request.POST['password']
    Admin=Admin_tb.objects.filter(Username=Username,Password=Password)
    Teacher=Teacher_tb.objects.filter(Username=Username,Password=Password)
    Parent=Parent_tb.objects.filter(Username=Username,Password=Password)
    if Admin.count()>0:
        request.session['id']=Admin[0].id
        return render(request,"Adminhome.html")
    elif Teacher.count()>0:
        status=Teacher[0].status
        if status=="approved":
            request.session['id']=Teacher[0].id
            return render(request,"Teacherhome.html")
        else:
            messages.add_message(request,messages.INFO,"Waiting for Approval")
            return redirect("login")
    elif Parent.count()>0:
        request.session['id']=Parent[0].id
        return render(request,"Parenthome.html")  
    else:
        messages.add_message(request,messages.INFO,"Invalid Username or Password")
        return redirect('/')
def ViewTeacher(request):
    tea=request.session['id']
    te=Teacher_tb.objects.filter(status="pending")
    return render(request,'viewteacher.html',{'teacher':te})
def details(request,id):
    teacher=Teacher_tb.objects.filter(id=id)
    return render(request,'details.html',{'teacher':teacher})
def approve(request,id):
    te=Teacher_tb.objects.filter(id=id).update(status='approved')
    return redirect('ViewTeacher')
def reject(request,id):
    te=Teacher_tb.objects.filter(id=id).update(status='reject')
    return redirect('ViewTeacher')
def ViewActivities(request):
    kids=Activity_tb.objects.all()
    return render(request,'ViewActivities.html',{'kids':kids})
def ViewEvents(request):
    events=Event_tb.objects.all()
    return render(request,'ViewEvents.html',{'Events':events})
def ViewFoodShedules(request):
    food=FoodShedule_tb.objects.all()
    return render(request,'ViewFoodShedules.html',{'food':food})
def ViewSponsershipDetails(request):
    Sponsership=sponsership_tb.objects.all()
    return render(request,'ViewSponsershipDetails.html',{'Sponsership': Sponsership})
def ForgotPassword(request):
    return render(request,'ForgotPassword.html')
def ForgotPasswordAction(request):
    Username=request.POST['username']
    # Password=request.POST['password']
    Teacher=Teacher_tb.objects.filter(Username=Username)
    Parent=Parent_tb.objects.filter(Username=Username)
    if Teacher.count()>0:
        return render(request,"Newpassword.html",{"data":Username})
    elif Parent.count()>0:
         return render(request,"Newpassword.html",{"data":Username})  
    else:
        return redirect('ForgotPassword')

def NewPasswordAction(request):
    Username=request.POST['username']
    Name=request.POST['name']
    Phoneno=request.POST['phoneno']
    Teacher=Teacher_tb.objects.filter(Username=Username,Name=Name,Phoneno=Phoneno)
    Parent=Parent_tb.objects.filter(Username=Username,Name=Name,Phoneno=Phoneno)
    if Teacher.count()>0:
        return render(request,"Enternewpassword.html",{"data":Username})
    elif Parent.count()>0:
        return render(request,"Enternewpassword.html",{"data":Username})  
    else:
        return redirect('index')
def EnternewpasswordAction(request):
    Username=request.POST['username']
    EnternewPassword=request.POST['enternewpassword']
    ConfirmPassword=request.POST['confirmpassword']
    if EnternewPassword==ConfirmPassword:
        Teacher=Teacher_tb.objects.filter(Username=Username)
        Parent=Parent_tb.objects.filter(Username=Username)
        if Teacher.count()>0:
            request.session['id']=Teacher[0].id
            Teacherid=request.session['id']
            Teacher=Teacher_tb.objects.filter(id=Teacherid).update(Password=EnternewPassword)
        else:
            request.session['id']=Parent[0].id
            Parentid=request.session['id']
            Parent=Parent_tb.objects.filter(id=Parentid).update(Password=EnternewPassword)
        messages.add_message(request,messages.INFO,"Password succesfull")
        request.session.flush() 
        return redirect('index')
    else:
        messages.add_message(request,messages.INFO,"Password doesn't match")
        return render(request,"Enternewpassword.html",{"data":Username})
def logout(request):
    return redirect('index')
   
