from django.db import models

# Create your models here.

class Burger(models.Model):  #Burger Model 클래스 정의
    name = models.CharField(max_length=20)  #문자열 CharField
    price = models.IntegerField(default=0)  #숫자형 IntegerField
    calories = models.IntegerField(default=0) #숫자형 IntegerField

    def __str__(self): #객체를 문자열로 표현하는 함수
        return self.name #name 속성을 반환