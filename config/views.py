#주문을 처리하는 직원
#python manage.py runserver 서버실행 명령어

from django.http import HttpResponse
from django.shortcuts import render

def main(request): # main 함수 정의
    return render(request, "main.html") # main.html을 렌더링
    #HttpResponse 대신 render 함수를 사용

def burger_list(request):# 새로운 View 함수 정의
    return render(request, "burger_list.html")
    #HttpResponse 대신 render 함수를 사용

