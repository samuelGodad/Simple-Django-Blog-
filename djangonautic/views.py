from django.http import HttpResponse
from django.shortcuts import render
def about(request):
    # return HttpResponse('this is about page after i  correct the rgulare expression ')
    return render(request,'about.html')
def homePage(request):
    # return HttpResponse("this is home page")
    return  render(request,'homePage.html')
    