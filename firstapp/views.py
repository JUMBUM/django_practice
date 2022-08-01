from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Curriculum
#django에서 sqlite에 입력하는 세가지 방식
def insert(request):
    msg = ''
    # 1-linux 입력
    Curriculum.objects.create(name = 'linux')
    msg = msg + '1번 입력 완료 <br>'
    # 2-python 입력
    c= Curriculum(name='python')
    c.save()
    msg = msg + '2번 입력 완료 <br>'
    # 3-html/css/js 입력
    Curriculum(name='python').save()
    msg = msg + '3번 입력 완료 <br>'
    # 4-django 입력
    Curriculum(name = 'django').save()
    msg = msg + '4번 입력 완료 <br>'
    return HttpResponse(msg)

##objects 데이터베이스 모델을 만드는 장고 라이브러리(컬럼들의 정보를 의미)
##create는 sql의 insert랑 같음

def show(request):
    curriculum = Curriculum.objects.all()
    result = ''
    for c in curriculum:
        result += c.name + '<br>'
    return HttpResponse(result)

## all은 sql의 *과 같음

##python과 html 언어를 render함수가 합쳐서 넘김
def show2(request):
    return render(request,
                "firstapp/show.html",{})
    
    
def show3(request):
    curriculum = Curriculum.objects.all()
    
    return render(request,
                  "firstapp/show2.html",
                  {"data" : curriculum})
    
    
    
def show4(request):
    curriculum = Curriculum.objects.all()
    
    return render(request,
                  "firstapp/show3.html",
                  {"data" : curriculum})