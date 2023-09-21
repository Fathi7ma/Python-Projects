from django.shortcuts import render
from django.http import HttpResponse
def demo(request):
    return render(request,"index.html")
#def operation(request):
   # x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
   # add=x+y
    #sub=x-y
    #mul=x*y
    #div=x/y
    #return render(request,"result.html",{'add':add,'sub':sub,'mul':mul,'div':div})


# Create your views here.
