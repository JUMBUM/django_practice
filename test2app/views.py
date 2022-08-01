from django.shortcuts import render

# Create your views here.

def show(request):
    return render(request,
                  "test2app/test2.html",{})
    
def show1(request):
    return render(request,
                  "test2app/test1.html",{})
    
    
def show2(request):
    return render(request,
                  "test2app/test3.html",{})