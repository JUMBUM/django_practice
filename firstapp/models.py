from django.db import models

class Curriculum(models.Model):
    name = models.CharField(max_length = 255)

# Create your models here.
# models.py는 무조건 클래스로 생성, 기본적으로 클래스 이름은 테이블 이름, name은 컬럼이 됨

# models 파일이 변경되면 항상 밑의 코드를 실행
# python manage.py makemigrations app이름
# python manage.py migrate