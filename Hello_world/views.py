from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("<H1>Hello World</H1>") # For HttpResponse
    mycontext = {'name':'Abhay'}
    return render(request, 'Home.html', mycontext)

def add(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    myvar = num1 + num2
    mycontext = {'result_var': myvar}
    return render(request, 'result.html', mycontext)
