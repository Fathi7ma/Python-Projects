from django.shortcuts import render,redirect
from SiteAdmin.models import*
from Parent.models import*
from Teacher.models import*
from django.contrib import messages

# Create your views here.
def parent(request):
    return render(request,'parent.html')
def parentAction(request):
    Name=request.POST['name']
    Gender=request.POST['gender']
    Address=request.POST['address']
    Phoneno=request.POST['phoneno']
    if len(request.FILES)>0:
        file=request.FILES['file']
    else:
        file="no pic"
    username=request.POST['username']
    password=request.POST['password']
    confirmpassword=request.POST['confirmpassword']
    new=Parent_tb(Name=Name,Gender=Gender,Address=Address,Phoneno=Phoneno,File=file,Username=username,Password=password,confirmpassword= confirmpassword)
    new.save()
    messages.add_message(request,messages.INFO,"Registeration succesfully")
    return redirect('parent')
def parentupdate(request):
    parent=request.session['id']
    #print(parent)
    pt=Parent_tb.objects.filter(id=parent)
    #print(pt)
    return render(request,'parentupdate.html',{'parent':pt})
def parentupdateAction(request):
    #id=request.POST['id']
    print(id)
    parent=request.session['id']
    print(parent)
    pt=Parent_tb.objects.filter(id=parent)
    Name=request.POST['name']
    Gender=request.POST['gender']
    Address=request.POST['address']
    Phone=request.POST['phone']
    if len(request.FILES)>0:
        img=request.FILES['file']
    else:
        img=pt[0].File
    Username=request.POST['username']
    password=request.POST['password']
    confirmpassword=request.POST['confirmpassword']
    new=Parent_tb.objects.filter(id=parent).update(Name=Name,Gender=Gender,Address=Address,Phoneno=Phone,Username=Username,Password=password,confirmpassword=confirmpassword)
    Parent_object=Parent_tb.objects.get(id=parent)
    Parent_object.File=img
    Parent_object.save()
    messages.add_message(request,messages.INFO,"Updation Successfull")
    return redirect('parentupdate')
def addstudent(request):
    return render(request,'student.html')
def studentAction(request):
    parentid=request.session['id']
    Name=request.POST['name']
    Gender=request.POST['gender']
    Age=request.POST['age']
    FatherName=request.POST['fathername']
    MotherName=request.POST['mothername']
    Address=request.POST['address']
    Phoneno=request.POST['phoneno']
    if len(request.FILES)>0:
        file=request.FILES['file']
    else:
        file="NO PIC"
    new=Student_tb(Name=Name,Gender=Gender,Age=Age,FatherName=FatherName,MotherName=MotherName,Address=Address,Phoneno=Phoneno,Image=file,Parentid_id=parentid)
    new.save()
    messages.add_message(request,messages.INFO,"Registeration succesfully")
    return redirect('addstudent')
def ViewStudent(request):
    Student=Student_tb.objects.all()
    return render(request,'ViewStudent.html',{'Student':Student})
def Deletestudent(request,id):
    Student=Student_tb.objects.filter(id=id).delete()
    return redirect('ViewStudent')
def StudentUpdate(request,id):
    #parentid=request.POST['id']
    Student=Student_tb.objects.filter(id=id)
    return render(request,'StudentUpdate.html',{'Student':Student})
def StudentUpdateAction(request):
    Parentid=request.session['id']
    student=request.POST['id']
    Student=Student_tb.objects.filter(id=student)
    if len(request.FILES)>0:
        img=request.FILES['file']
    else:
        img=Student[0].Image
    Name=request.POST['name']
    Gender=request.POST['gender']
    Age=request.POST['age']
    FatherName=request.POST['fathername']
    MotherName=request.POST['mothername']
    Address=request.POST['address']
    Phoneno=request.POST['phone']
    new=Student_tb.objects.filter(id=student).update(Name=Name,Gender=Gender,Age=Age,FatherName=FatherName,MotherName=MotherName,Address=Address,Phoneno=Phoneno,Parentid=Parentid)
    Student_object=Student_tb.objects.get(id=student)
    Student_object.Image=img
    Student_object.save()
    messages.add_message(request,messages.INFO,"Updation succesfully")
    return redirect('ViewStudent') 
def ViewsAttendence(request):
    Attendence=Attendence_tb.objects.all()
    present=Present_tb.objects.all()
    absent=Absent_tb.objects.all()
    return render(request,'ViewsAttendence.html',{'Attendence':Attendence,'present':present,'absent':absent})
def searchbydates(request):
    search=request.POST['date']
    Attendence=Attendence_tb.objects.filter(Date__istartswith=search)
    present=Present_tb.objects.filter(Date__istartswith=search)
    absent=Absent_tb.objects.filter(Date__istartswith=search)
    return render(request,'ViewsAttendence.html',{'Attendence':Attendence,'present':present,'absent':absent})
    
def ViewActivity(request):
    kids=Activity_tb.objects.all()
    return render(request,'ViewActivity.html',{'kid':kids})
def Viewevent(request):
    Event=Event_tb.objects.all()
    return render(request,'ViewsEvent.html',{'event':Event})
def ViewsFoodShedule(request):
    food=FoodShedule_tb.objects.all()
    return render(request,'ViewsFoodShedule.html',{'food':food})
def ViewsDailyShedule(request):
    DailyShedule=DailyActivity_tb.objects.all()
    return render(request,'ViewsDailyShedule.html',{'DailyShedule':DailyShedule})
def Sponsership(request):
    return render(request,'Sponsership.html')
def SponsershipAction(request):
    SponserName=request.POST['sponsership']
    Job=request.POST['job']
    Address=request.POST['address']
    SponsershipItem=request.POST['sponseritem']
    sponser=sponsership_tb(SponserName=SponserName,Job=Job,Address=Address,SponserItem=SponsershipItem)
    sponser.save()
    messages.add_message(request,messages.INFO,"Registeration succesfully")
    return redirect('Sponsership')
def ViewSponsership(request):
    Sponsership=sponsership_tb.objects.all()
    return render(request,'ViewSponsership.html',{'Sponsership': Sponsership})
def DeleteSponsership(request,id):
    Sponsership=sponsership_tb.objects.filter(id=id).delete()
    return redirect('ViewSponsership')
def SponsershipUpdate(request,id):
    #parentid=request.POST['id']
    Sponsership=sponsership_tb.objects.filter(id=id)
    return render(request,'SponsershipUpdate.html',{'Sponsership': Sponsership})
def SponsershipUpdateAction(request):
    sponser=request.POST['id']
    Sponser=sponsership_tb.objects.filter(id=sponser)
    SponserName=request.POST['sponser']
    Job=request.POST['job']
    Address=request.POST['address']
    SponsershipItem=request.POST['sponseritem']
    sponser=sponsership_tb.objects.filter(id=sponser).update(SponserName=SponserName,Job=Job,Address=Address,SponserItem=SponsershipItem)
    Sponser_object=sponsership_tb.objects.get(id=sponser)
    Sponser_object.save()
    messages.add_message(request,messages.INFO,"Updation succesfully")
    return redirect('ViewSponsership')  
def ParentChangepassword(request):
    Parent=request.session['id']
    Parent=Parent_tb.objects.filter(id=Parent)
    return render(request,'ParentChangepassword.html')   
def ParentChangepasswordAction(request):
    Parent=request.session['id']
    OldPassword=request.POST['oldpassword']
    NewPassword=request.POST['newpassword']
    ConfirmPassword=request.POST['confirmpassword']
    pa=Parent_tb.objects.filter(id=Parent,Password=OldPassword)
    if pa.count()>0:
        if NewPassword==ConfirmPassword:
            te=Parent_tb.objects.filter(id=Parent).update(Password=NewPassword)
            messages.add_message(request,messages.INFO,"Updated succesfully")
        else:
            messages.add_message(request,messages.INFO,"Not Equal")
    else:
         messages.add_message(request,messages.INFO,"Current Password Not Equal")
    return redirect('ParentChangepassword')
def Vaccinationid(request,id):
    vace=Student_tb.objects.filter(id=id)
    return render(request,'Vaccination.html',{'vace':vace})
def VaccinationAction(request):
    parent=request.session['id']
    sid=request.POST['id']
    Date=request.POST['date']
    VaccinationName=request.POST['vaccinationname']
    Place=request.POST['place']
    vaccination=Vaccination_tb(studentid_id=sid,Date=Date,VaccinationName=VaccinationName,Place=Place)
    vaccination.save()
    messages.add_message(request,messages.INFO,"Registeration succesfully")
    return redirect('ViewStudent')
def ViewVaccination(request,id):
    Vaccination=Vaccination_tb.objects.filter(studentid=id)
    return render(request,'ViewVaccination.html',{'Vaccination':Vaccination})




