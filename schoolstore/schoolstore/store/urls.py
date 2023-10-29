from . import views
from django.urls import path
urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('loginAction/',views.loginAction,name='loginAction'),
    path('register/',views.register,name='register'),
    path('registerAction/',views.registerAction,name='registerAction'),
    # path('loginpage/',views.loginpage,name='loginpage'),
    # path('loginpageAction/',views.loginpageAction,name='loginpageAction'),
    path('form/',views.form,name='form'),
    path('formAction/', views.formAction, name='formAction'),
    path('logout/', views.logout, name='logout'),
]