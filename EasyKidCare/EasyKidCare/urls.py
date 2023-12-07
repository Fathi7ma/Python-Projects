"""EasyKidCare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Parent import views as Parentview
from Teacher import views as Teacherview
from SiteAdmin import views as SiteAdminview
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',SiteAdminview.index,name="index"),
    path('login/',SiteAdminview.login,name='login'),
    path('loginAction/',SiteAdminview.loginAction,name='loginAction'),
    path('register/',Teacherview.register,name='register'),
    path('registerAction/',Teacherview.registerAction,name='registerAction'),
    path('parent/',Parentview.parent,name='parent'),
    path('parentAction/',Parentview.parentAction,name='parentAction'),
    path('teacherupdate/',Teacherview.teacherupdate,name='teacherupdate'),
    path('parentupdate/',Parentview.parentupdate,name='parentupdate'),
    path('parentupdateAction/',Parentview.parentupdateAction,name='parentupdateAction'),
    path('teacherupdateAction/',Teacherview.teacherupdateAction,name='teacherupdateAction'),
    path('ViewTeacher/',SiteAdminview.ViewTeacher,name='ViewTeacher'),
    path('details<int:id>/',SiteAdminview.details,name='details'),
    path('approve<int:id>/',SiteAdminview.approve,name='approve'),
    path('reject<int:id>/',SiteAdminview.reject,name='reject'),
    path('ViewParent/',Teacherview.ViewParent,name='ViewParent'),
    path('Parentdetails<int:id>/',Teacherview.Parentdetails,name='Parentdetails'),
    path('parentapprove<int:id>/',Teacherview.parentapprove,name='parentapprove'),
    path('parentreject<int:id>/',Teacherview.parentreject,name='parentreject'),
    path('addstudent/',Parentview.addstudent,name='addstudent'),
    path('studentAction/',Parentview.studentAction,name='studentAction'),
    path('ViewStudent/',Parentview.ViewStudent,name='ViewStudent'),
    path('Deletestudent<int:id>/',Parentview.Deletestudent,name='Deletestudent'),
    path('StudentUpdate<int:id>/',Parentview.StudentUpdate,name='StudentUpdate'),
    path('StudentUpdateAction/',Parentview.StudentUpdateAction,name='StudentUpdateAction'),
    path('ViewStudents/',Teacherview.ViewStudents,name='ViewStudents'),
    path('studentapprove<int:id>/',Teacherview.studentapprove,name='studentapprove'),
    path('studentreject<int:id>/',Teacherview.studentreject,name='studentreject'),
    path('AddActivities/',Teacherview.AddActivities,name='AddActivities'),
    path('AddActivitiesAction/',Teacherview.AddActivitiesAction,name='AddActivitiesAction'),
    path('ViewActivities/',SiteAdminview.ViewActivities,name='ViewActivities'),
    path('ViewActivity/',Parentview.ViewActivity,name='ViewActivity'),
    path('ViewsActivity/',Teacherview.ViewsActivity,name='ViewsActivity'),
    path('DeleteActivity<int:id>/',Teacherview.DeleteActivity,name='DeleteActivity'),
    path('ActivityUpdate<int:id>/',Teacherview.ActivityUpdate,name='ActivityUpdate'),
    path('ActivityUpdateAction/',Teacherview.ActivityUpdateAction,name='ActivityUpdateAction'),
    path('AddDailyShedule/',Teacherview.AddDailyShedule,name='AddDailyShedule'),
    path('AddDailySheduleAction/',Teacherview.AddDailySheduleAction,name='AddDailySheduleAction'),
    path('ViewDailyShedule/',Teacherview.ViewDailyShedule,name='ViewDailyShedule'),
    path('DeleteDailyShedule<int:id>/',Teacherview.DeleteDailyShedule,name='DeleteDailyShedule'),
    path('DailySheduleUpdate<int:id>/',Teacherview.DailySheduleUpdate,name='DailySheduleUpdate'),
    path('DailySheduleUpdateAction/',Teacherview.DailySheduleUpdateAction,name='DailySheduleUpdateAction'),
    path('ViewsDailyShedule/',Parentview.ViewsDailyShedule,name='ViewsDailyShedule'),
    path('AddEvent/',Teacherview.AddEvent,name='AddEvent'),
    path('AddEventAction/',Teacherview.AddEventAction,name='AddEventAction'),
    path('ViewEvent/',Teacherview.ViewEvent,name='ViewEvent'),
    path('ViewEvents/',SiteAdminview.ViewEvents,name='ViewEvents'),
    path('Viewevent/',Parentview.Viewevent,name='Viewevent'),
    path('DeleteEvent<int:id>/',Teacherview.DeleteEvent,name='DeleteEvent'),
    path('EventUpdate<int:id>/',Teacherview.EventUpdate,name='EventUpdate'),
    path('EventUpdateAction/',Teacherview.EventUpdateAction,name='EventUpdateAction'),
    path('Attendence/',Teacherview.Attendence,name='Attendence'),
    path('AttendenceAction/',Teacherview.AttendenceAction,name='AttendenceAction'),
    path('ViewAttendence/',Teacherview.ViewAttendence,name='ViewAttendence'),
    path('ViewsAttendence/',Parentview.ViewsAttendence,name='ViewsAttendence'),
    path('searchbydate/',Teacherview.searchbydate,name='searchbydate'),
    path('searchbydates/',Parentview.searchbydates,name='searchbydates'),
    path('FoodShedule/',Teacherview.FoodShedule,name='FoodShedule'),
    path('FoodSheduleAction/',Teacherview.FoodSheduleAction,name='FoodSheduleAction'),
    path('ViewFoodShedule/',Teacherview.ViewFoodShedule,name='ViewFoodShedule'),
    path('ViewsFoodShedule/',Parentview.ViewsFoodShedule,name='ViewsFoodShedule'),
    path('ViewFoodShedules/',SiteAdminview.ViewFoodShedules,name='ViewFoodShedules'),
    path('DeleteFoodShedule<int:id>/',Teacherview.DeleteFoodShedule,name='DeleteFoodShedule'),
    path('FoodSheduleUpdate<int:id>/',Teacherview.FoodSheduleUpdate,name='FoodSheduleUpdate'),
    path('FoodSheduleUpdateAction/',Teacherview.FoodSheduleUpdateAction,name='FoodSheduleUpdateAction'),
    path('Sponsership/',Parentview.Sponsership,name='Sponsership'),
    path('SponsershipAction/',Parentview.SponsershipAction,name='SponsershipAction'),
    path('ViewSponsership/',Parentview.ViewSponsership,name='ViewSponsership'),
    path('DeletesSponsership<int:id>/',Parentview.DeleteSponsership,name='DeleteSponsership'),
    path('SponsershipUpdate<int:id>/',Parentview.SponsershipUpdate,name='SponsershipUpdate'),
    path('SponsershipUpdateAction/',Parentview.SponsershipUpdateAction,name='SponsershipUpdateAction'),
    path('ViewSponsershipDetails/',SiteAdminview.ViewSponsershipDetails,name='ViewSponsershipDetails'),
    path('Viewssponsership/',Teacherview.Viewssponsership,name='Viewssponsership'),
    path('ForgotPassword/',SiteAdminview.ForgotPassword,name='ForgotPassword'),
    path('ForgotPasswordAction/',SiteAdminview.ForgotPasswordAction,name='ForgotPasswordAction'), 
    path('NewPasswordAction/',SiteAdminview.NewPasswordAction,name='NewPasswordAction'),
    path('EnternewpasswordAction/',SiteAdminview.EnternewpasswordAction,name='EnternewpasswordAction'),
    path('ChangePassword/',Teacherview.ChangePassword,name='ChangePassword'),
    path('ChangePasswordAction/',Teacherview.ChangePasswordAction,name='ChangePasswordAction'),
    path('ParentChangepassword/',Parentview.ParentChangepassword,name='ParentChangepassword'),
    path('ParentChangepasswordAction/',Parentview.ParentChangepasswordAction,name='ParentChangepasswordAction'),
    path('AddMother/',Teacherview.AddMother,name='AddMother'),
    path('AddMotherAction/',Teacherview.AddMotherAction,name='AddMotherAction'),
    path('ViewMother/',Teacherview.ViewMother,name='ViewMother'),
    path('DeleteMother<int:id>/',Teacherview.DeleteMother,name='DeleteMother'),
    path('MotherUpdate<int:id>/',Teacherview.MotherUpdate,name='MotherUpdate'),
    path('MotherUpdateAction/',Teacherview.MotherUpdateAction,name='MotherUpdateAction'),
    path('ViewTHR<int:id>/',Teacherview.ViewTHR,name='ViewTHR'),
    path('moreinformation<int:id>/',Teacherview.moreinformation,name='moreinformation'),
    path('Nutritions/',Teacherview.Nutritions,name='Nutritions'),
    path('NutritionsAction/',Teacherview.NutritionsAction,name='NutritionsAction'),
    path('THR/',Teacherview.THR,name='THR'),
    path('THRAction/',Teacherview.THRAction,name='THRAction'),
    path('LactatingWoman/',Teacherview.LactatingWoman,name='LactatingWoman'),
    path('LactatingWomanAction/',Teacherview.LactatingWomanAction,name='LactatingWomanAction'),
    path('ViewLactatingWoman/',Teacherview.ViewLactatingWoman,name='ViewLactatingWoman'),
    path('DeleteLactatingWoman<int:id>/',Teacherview.DeleteLactatingWoman,name='DeleteLactatingWoman'),
    path('LactatingWomanUpdate<int:id>/',Teacherview.LactatingWomanUpdate,name='LactatingWomanUpdate'),
    path('LactatingWomanUpdateAction/',Teacherview.LactatingWomanUpdateAction,name='LactatingWomanUpdateAction'),
    path('ViewsTHR<int:id>/',Teacherview.ViewsTHR,name='ViewsTHR'),
     # path('Vaccination/',Parentview.Vaccination,name='Vaccination'),
    path('VaccinationAction/',Parentview.VaccinationAction,name='VaccinationAction'),
    path('Vaccinationid<int:id>/',Parentview.Vaccinationid,name='Vaccinationid'),
    path('ViewVaccination<int:id>/',Parentview.ViewVaccination,name='ViewVaccination'),
    path('ViewsVaccination<int:id>/',Teacherview.ViewsVaccination,name='ViewsVaccination'),
    path('GrowthDetails/',Teacherview.GrowthDetails,name='GrowthDetails'),
    path('GrowthDetailsAction/',Teacherview.GrowthDetailsAction,name='GrowthDetailsAction'),
    path('ViewGrowthDetails/',Teacherview.ViewGrowthDetails,name='ViewGrowthDetails'),
    path('logout/',SiteAdminview.logout,name='logout'),
   
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)






