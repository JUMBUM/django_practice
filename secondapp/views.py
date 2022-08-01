from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.
def insert(request):
    msg = '데이터 입력 완료'
    Course(name = '데이터분석', cnt = 20).save()
    Course(name = '데이터수집', cnt = 19).save()
    Course(name = '웹개발', cnt = 18).save()
    Course(name = '인공지능', cnt = 17).save()
    return HttpResponse(msg)
    
    
def show(request):
    course = Course.objects.all()
    result = ''
    for c in course:
        result += c.name + '<br>'
    return HttpResponse(result)

def show2(request):
    course = Course.objects.all()
    
    return render(request,
                  "secondapp/show2.html",
                  {"data" : course})
    

    