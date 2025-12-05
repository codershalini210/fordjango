from django.shortcuts import render
from django.http import HttpResponse
def about(request):
    return render(request,"pages/about.html")
    # return HttpResponse("hello from  about us page")
def contact(request):
    return HttpResponse("this is contact us page")
def home(request):
    return HttpResponse("home page ")
# Create your views here.
