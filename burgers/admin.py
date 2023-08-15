from django.contrib import admin
from burgers.models import Burger
# Register your models here.

@admin.register(Burger) #Burger 모델을 admin 사이트에 등록
class BurgerAdmin(admin.ModelAdmin): #BurgerAdmin 클래스 정의
    pass

