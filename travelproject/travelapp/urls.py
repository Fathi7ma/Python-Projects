from.import views
from django.urls import path
urlpatterns=[
    path('',views.demo,name='demo'),
    #path('add/',views.operation,name='operation')
    ]

