from django.shortcuts import render,redirect
from SiteAdmin.models import*
from Parent.models import*
from Teacher.models import*
from django.contrib import messages

# Create your views here.
def register(request):
    return render(request,'register.html')
def registerAction(request):
    Name=request.POST['name']
    Age=request.POST['age']
    Phoneno=request.POST['phoneno']
    Gender=request.POST['gender']
    Address=request.POST['address']
    if len(request.FILES)>0:
        file=request.FILES['file']
    else:
        file="no pic"
    Email=request.POST['email']
    Qualification=request.POST['qualifications']
    username=request.POST['username']
    password=request.POST['password']
    confirmpassword=request.POST['confirmpassword']
    teacher=Teacher_tb(Name=Name,Age=Age,Phoneno=Phoneno,Gender=Gender,Address=Address,Email=Email,Qualifications=Qualification,Username=username,Password=password,confirmpassword=confirmpassword,File=file)
    teacher.save()
    messages.add_message(request,messages.INFO,"Registeration succesfully")
    return redirect('register')
def teacherupdate(request):
    teacher=request.session['id']
    te=Teacher_tb.objects.filter(id=teacher)
    return render(request,'teacherupdate.html',{'teacher':te})
def teacherupdateAction(request):
    #id=request.POST['id']
    print(id)
    teacher=request.session['id']
    print(teacher)
    pt=Teacher_tb.objects.filter(id=teacher)
    Name=request.POST['name']
    Age=request.POST['age']
    Phone=request.POST['phone']
    Gender=request.POST['gender']
    Address=request.POST['address']
    if len(request.FILES)>0:
        img=request.FILES['file']
    else:
        img=pt[0].File
    Email=request.POST['email']
    Qualifications=request.POST['qualifications']
    Username=request.POST['username']
    password=request.POST['password']
    confirmpassword=request.POST['confirmpassword']
    new=Teacher_tb.objects.filter(id=teacher).update(Name=Name,Age=Age,Phoneno=Phone,Gender=Gender,Address=Address,Email=Email,Qualifications=Qualifications,Username=Username,Password=password,confirmpassword=confirmpassword)
    Teacher_object=Teacher_tb.objects.get(id=teacher)
    Teacher_object.File=img
    Teacher_object.save()
    messages.add_message(request,messages.INFO,"Updation Successfull")
    return redirect('teacherupdate')
def ViewParent(request):
    pea=request.session['id']
    pa=Parent_tb.objects.filter(status="pending")
    return render(request,'ViewParent.html',{'parent':pa})
def Parentdetails(request,id):
    parent=Parent_tb.objects.filter(id=id)
    return render(request,'parentdetails.html',{'parent':parent})
def parentapprove(request,id):
    pa=Parent_tb.objects.filter(id=id).update(status='Parentapprove')
    return redirect('ViewParent')
def parentreject(request,id):
    te=Parent_tb.objects.filter(id=id).update(status='Parentreject')
    return redirect('ViewParent')   
def ViewStudents(request):
    st=Student_tb.objects.all()
    return render(request,'ViewStudents.html',{'Student':st})
def studentapprove(request,id):
    st=Student_tb.objects.filter(id=id).update(status='Studentapprove')
    return redirect('ViewStudents')
def studentreject(request,id):
    sa=Student_tb.objects.filter(id=id).update(status='Studentreject')
    return redirect('ViewStudents')   
def AddActivities(request):
    return render(request,'Activities.html')
def AddActivitiesAction(request):
    Date=request.POST['date']
    Item=request.POST['item']
    Description=request.POST['description']
    if len(request.FILES)>0:
        file=request.FILES['file']
    else:
        file="NO PIC"
    activities=Activity_tb(Date=Date,Item=Item,Description=Description,File=file)
    activities.save()
    messages.add_message(request,messages.INFO,"Registeration succesfully")
    return redirect('AddActivities')
def ViewsActivity(request):
    kids=Activity_tb.objects.all()
    return render(request,'ViewsActivity.html',{'kids':kids})
def DeleteActivity(request,id):
    Activity=Activity_tb.objects.filter(id=id).delete()
    return redirect('ViewsActivity')
def ActivityUpdate(request,id):
    ##activity=request.session['id']
    activity=Activity_tb.objects.filter(id=id)
    return render(request,'ActivityUpdate.html',{'activity':activity})
def ActivityUpdateAction(request):
    id=request.POST['id']
    activity=request.POST['id']
    print(activity)
    at=Activity_tb.objects.filter(id=activity)
    Date=request.POST['date']
    Item=request.POST['item']
    Description=request.POST['description']
   
    if len(request.FILES)>0:
        img=request.FILES['file']
    else:
        img=at[0].File
   
    new=Activity_tb.objects.filter(id=activity).update(Date=Date,Item=Item,Description=Description)
    Activity_object=Activity_tb.objects.get(id=activity)
    Activity_object.File=img
    Activity_object.save()
    messages.add_message(request,messages.INFO,"Updation Successfull")
    return redirect('ViewsActivity')
def AddDailyShedule(request):
    return render(request,'DailyShedule.html')
def AddDailySheduleAction(request):
    Events=request.POST['activity']
    Program=request.POST['food']
    Date=request.POST['date']
    Time=request.POST['time']
    Games=request.POST['games']
    DailyShedule=DailyActivity_tb(Activity=Events,Food=Program,Games=Games,Date=Date,SleepingTime=Time)
    DailyShedule.save()
    messages.add_message(request,messages.INFO,"Registeration succesfully")
    return redirect('AddDailyShedule')
def ViewDailyShedule(request):
    DailyShedule=DailyActivity_tb.objects.all()
    return render(request,'ViewDailyShedule.html',{'DailyShedule':DailyShedule})
def DeleteDailyShedule(request,id):
    DailyShedule=DailyActivity_tb.objects.filter(id=id).delete()
    return redirect('ViewDailyShedule')
def DailySheduleUpdate(request,id):
    #Event=request.session['id']
    DailyShedule=DailyActivity_tb.objects.filter(id=id)
    return render(request,'DailySheduleUpdate.html',{'DailyShedule':DailyShedule})
def DailySheduleUpdateAction(request):
    #id=request.POST['id']
    print(id)
    DailyShedule=request.POST['id']
    ds=DailyActivity_tb.objects.filter(id=DailyShedule)
    Activity=request.POST['activity']
    Food=request.POST['food']
    Games=request.POST['games']
    SleepingTime=request.POST['sleepingtime'] 
    Date=request.POST['date']
    DailyShedule=DailyActivity_tb.objects.filter(id=DailyShedule).update(Activity=Activity,Food=Food,Games=Games,SleepingTime=SleepingTime,Date=Date,)
    messages.add_message(request,messages.INFO,"Updation Successfull")
    return redirect('ViewDailyShedule')

def AddEvent(request):
    return render(request,'Events.html')  
def AddEventAction(request):
    Event_Name=request.POST['event']
    Description=request.POST['description']
    Venue=request.POST['venue']
    Date=request.POST['date']
    Food=request.POST['food'] 
    Event=Event_tb(Event_name=Event_Name,Description=Description,Venue=Venue,Date=Date,Food=Food)
    Event.save()
    messages.add_message(request,messages.INFO,"Registeration succesfully")
    return redirect('AddEvent')
def ViewEvent(request):
    event=Event_tb.objects.all()
    return render(request,'ViewEvent.html',{'Event':event})
def DeleteEvent(request,id):
    Event=Event_tb.objects.filter(id=id).delete()
    return redirect('ViewEvent')
def EventUpdate(request,id):
    #Event=request.session['id']
    event=Event_tb.objects.filter(id=id)
    return render(request,'EventUpdate.html',{'Event':event})
def EventUpdateAction(request):
    #id=request.POST['id']
    print(id)
    event=request.POST['id']
    
    pt=Event_tb.objects.filter(id=event)
    Event_Name=request.POST['event']
    Description=request.POST['description']
    Venue=request.POST['venue']
    Date=request.POST['date']
    Food=request.POST['food'] 
    new=Event_tb.objects.filter(id=event).update(Event_name=Event_Name,Description=Description,Venue=Venue,Date=Date,Food=Food)
    messages.add_message(request,messages.INFO,"Updation Successfull")
    return redirect('ViewEvent')
def Attendence(request):
    students=Student_tb.objects.all()
    return render(request,'Attendence.html',{'Student':students})
def AttendenceAction(request):
    Date=request.POST['date']
    dat=Attendence_tb(Date=Date)
    allstudents=Student_tb.objects.values_list('id',flat=True)
    dat.save()
    check=request.POST.getlist('checkbox')
    checkedmembers=list(map(int,check))
    unchecked=list(set(allstudents)-set(checkedmembers))
    for c in checkedmembers:
        p=Student_tb.objects.get(id=c)
        pr=Present_tb(Attendenceid_id=dat.id,Studentid=p,Date=dat.Date)
        pr.save()
    for d in unchecked:
        p=Student_tb.objects.get(id=d)
        pr=Absent_tb(Attendenceid_id=dat.id,Studentid=p,Date=dat.Date)
        pr.save()
    # return redirect('Attendence')
    messages.add_message(request,messages.INFO,"Registeration succesfully")
    return redirect('Attendence')
def ViewAttendence(request):
    Attendence=Attendence_tb.objects.all()
    present=Present_tb.objects.all()
    absent=Absent_tb.objects.all()
    return render(request,'ViewAttendence.html',{'Attendence':Attendence,'present':present,'absent':absent})
def searchbydate(request):
    search=request.POST['date']
    Attendence=Attendence_tb.objects.filter(Date__istartswith=search)
    present=Present_tb.objects.filter(Date__istartswith=search)
    absent=Absent_tb.objects.filter(Date__istartswith=search)
    return render(request,'ViewAttendence.html',{'Attendence':Attendence,'present':present,'absent':absent})
    
def FoodShedule(request):
    return render(request,'FoodShedule.html')  
def FoodSheduleAction(request):
    Date=request.POST['date']
    Snack=request.POST['snack']
    Lunch=request.POST['lunch']
    Eveningsnack=request.POST['eveningsnack']
    food=FoodShedule_tb(Date=Date,Snack=Snack,Lunch=Lunch,Eveningsnack=Eveningsnack)
    food.save()
    messages.add_message(request,messages.INFO,"Registeration succesfully")
    return redirect('FoodShedule')
def ViewFoodShedule(request):
    food=FoodShedule_tb.objects.all()
    return render(request,'ViewFoodShedule.html',{'food':food})
def DeleteFoodShedule(request,id):
    food=FoodShedule_tb.objects.filter(id=id).delete()
    return redirect('ViewFoodShedule')
def FoodSheduleUpdate(request,id):
    #Event=request.session['id']
    food=FoodShedule_tb.objects.filter(id=id)
    return render(request,'FoodSheduleUpdate.html',{'food':food})
def FoodSheduleUpdateAction(request):
    #id=request.POST['id']
    print(id)
    food=request.POST['id']
    
    fd=FoodShedule_tb.objects.filter(id=food)
    Date=request.POST['date']
    Snack=request.POST['snack']
    Lunch=request.POST['lunch']
    Eveningsnack=request.POST['eveningsnack']
    new=FoodShedule_tb.objects.filter(id=food).update(Date=Date,Snack=Snack,Lunch=Lunch,Eveningsnack=Eveningsnack)
    messages.add_message(request,messages.INFO,"Updation Successfull")
    return redirect('ViewFoodShedule')
def Viewssponsership(request):
    Sponsership=sponsership_tb.objects.all()
    return render(request,'Viewssponsership.html',{'Sponsership': Sponsership})
def ChangePassword(request):
    Teacher=request.session['id']
    Teacher=Teacher_tb.objects.filter(id=Teacher)
    return render(request,'ChangePassword.html') 
def ChangePasswordAction(request):
    Teacher=request.session['id']
    OldPassword=request.POST['oldpassword']
    NewPassword=request.POST['newpassword']
    ConfirmPassword=request.POST['confirmpassword']
    te=Teacher_tb.objects.filter(id=Teacher,Password=OldPassword)
    if te.count()>0:
        if NewPassword==ConfirmPassword:
            te=Teacher_tb.objects.filter(id=Teacher).update(Password=NewPassword)
            messages.add_message(request,messages.INFO,"Updated succesfully")
        else:
            messages.add_message(request,messages.INFO,"Not Equal")
    else:
         messages.add_message(request,messages.INFO,"Current Password Not Equal")
    return redirect('ChangePassword')
def AddMother(request):
    nutrition=Nutritions_tb.objects.all()
    thr=THR_tb.objects.all()
    return render(request,'AddMother.html',{'nutrition':nutrition,'thr':thr})
def AddMotherAction(request):
    Mothername=request.POST['Mothername']
    Dob=request.POST['dob']
    Details=request.POST['Details']
    Address=request.POST['Address']
    Phoneno=request.POST['Phoneno']
    Height=request.POST['height']
    Weight=request.POST['weight']
    nutritious=request.POST['nutritious']
    Hemoglobin=request.POST['hemoglobin']
    Item=request.POST['thr']
    Mother=Mother_tb(Mother_name=Mothername,Dob=Dob,Details=Details,Address=Address,Phoneno=Phoneno,Height=Height,Weight=Weight,Hemoglobin=Hemoglobin, Nutritions_id=nutritious,Thr_id=Item)
    Mother.save()
    messages.add_message(request,messages.INFO,"Registeration succesfully")
    return redirect('AddMother')
def ViewMother(request):
    mother=Mother_tb.objects.all()
    return render(request,'ViewMother.html',{'mother': mother})
def DeleteMother(request,id):
    mother=Mother_tb.objects.filter(id=id).delete()
    return redirect('ViewMother')
def MotherUpdate(request,id):
    #Event=request.session['id']
    mother=Mother_tb.objects.filter(id=id)
    return render(request,'MotherUpdate.html',{'mother':mother})
def MotherUpdateAction(request):
    #id=request.POST['id']
    print(id)
    mother=request.POST['id']
    
    mr=Mother_tb.objects.filter(id=mother)
    Mother_name=request.POST['mothername']
    Dob=request.POST['dob']
    Details=request.POST['details']
    Phoneno=request.POST['phoneno']
    Address=request.POST['address']
    Height=request.POST['height']
    Weight=request.POST['weight']
    Hemoglobin=request.POST['hemoglobin']
    new=Mother_tb.objects.filter(id=mother).update(Mother_name=Mother_name,Dob=Dob,Details=Details,Phoneno=Phoneno,Address=Address,Height=Height,Weight=Weight,Hemoglobin=Hemoglobin)
    messages.add_message(request,messages.INFO,"Updation Successfull")
    return redirect('ViewMother')
def ViewTHR(request,id):
    thr=Mother_tb.objects.filter(id=id)
    return render(request,'ViewTHR.html',{'thr':thr})
def moreinformation(request,id):
    mother=Mother_tb.objects.filter(id=id)
    return render(request,'MotherDetails.html',{'mother':mother})
def Nutritions(request):
    return render(request,'Nutritions.html')
def NutritionsAction(request):
    Name=request.POST['name']
    nutritions=Nutritions_tb(Name=Name)
    nutritions.save()
    messages.add_message(request,messages.INFO,"Registeration succesfully")
    return redirect('Nutritions')
def LactatingWoman(request):
    #nutrition=Nutritions_tb.objects.all()
    thr=THR_tb.objects.all()
    return render(request,'LactatingWoman.html',{'thr':thr})
def LactatingWomanAction(request):
    Name=request.POST['name']
    Dob=request.POST['dob']
    Phoneno=request.POST['Phoneno']
    Deliverydate=request.POST['deliverydate']
    Infantgender=request.POST['infantgender']
    #nutritious=request.POST['nutritious']
    Item=request.POST['thr']
    woman=LactatingWoman_tb(Name=Name,Dob=Dob,Phoneno=Phoneno,Deliverydate=Deliverydate,Infantgender=Infantgender,Thr_id=Item)
    woman.save()
    messages.add_message(request,messages.INFO,"Registeration succesfully")
    return redirect('LactatingWoman')
def ViewLactatingWoman(request):
    woman=LactatingWoman_tb.objects.all()
    return render(request,'ViewLactatingWoman.html',{'woman': woman})
def DeleteLactatingWoman(request,id):
    woman=LactatingWoman_tb.objects.filter(id=id).delete()
    return redirect('ViewLactatingWoman')
def LactatingWomanUpdate(request,id):
    #Event=request.session['id']
    woman=LactatingWoman_tb.objects.filter(id=id)
    return render(request,'LactatingWomanUpdate.html',{'woman':woman})
def LactatingWomanUpdateAction(request):
    #id=request.POST['id']
    print(id)
    woman=request.POST['id']
    
    wn=LactatingWoman_tb.objects.filter(id=woman)
    Name=request.POST['name']
    Dob=request.POST['dob']
    Phoneno=request.POST['Phoneno']
    Deliverydate=request.POST['deliverydate']
    Infantgender=request.POST['infantgender']
    # Item=request.POST['thr']
    new=LactatingWoman_tb.objects.filter(id=woman).update(Name=Name,Dob=Dob,Phoneno=Phoneno,Deliverydate=Deliverydate,Infantgender=Infantgender)
    messages.add_message(request,messages.INFO,"Updation Successfull")
    return redirect('ViewLactatingWoman')
def ViewsTHR(request,id):
    thr=LactatingWoman_tb.objects.filter(id=id)
    return render(request,'ViewsTHR.html',{'thr':thr})
def ViewsVaccination(request,id):
    Vaccination=Vaccination_tb.objects.filter(studentid=id)
    return render(request,'ViewsVaccination.html',{'Vaccination':Vaccination})
def THR(request):
    return render(request,'THR.html')
def THRAction(request):
    Item=request.POST['item']
    Quantity=request.POST['quantity']
    thr=THR_tb(Item=Item,Quantity=Quantity)
    thr.save()
    messages.add_message(request,messages.INFO,"Registeration succesfully")
    return redirect('THR')
def ViewsVaccination(request,id):
    Vaccination=Vaccination_tb.objects.filter(studentid=id)
    return render(request,'ViewsVaccination.html',{'Vaccination':Vaccination})
def GrowthDetails(request):
    return render(request,'GrowthDetails.html')
def GrowthDetailsAction(request):
    Name=request.POST['name']
    Date_of_birth=request.POST['dob']
    Birth_reg_no=request.POST['reg_no']
    Fathername=request.POST['father']
    Mothername=request.POST['mother']
    Family_survey_regno=request.POST['survey']
    Growth=GrowthDetails_tb(Name=Name,Date_of_birth=Date_of_birth,Birth_reg_no=Birth_reg_no,Fathername=Fathername,Mothername=Mothername,Family_survey_regno=Family_survey_regno)
    Growth.save()
    messages.add_message(request,messages.INFO,"Registeration succesfully")
    return redirect('GrowthDetails')
def ViewGrowthDetails(request):
    Growth=GrowthDetails_tb.objects.all()
    return render(request,'ViewGrowthDetails.html',{'Growth': Growth})