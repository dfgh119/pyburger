#주문을 받는 직원
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from config.views import main #config 폴더의 views.py를 import

#urlpatterns는 리스트, 각 path는 메뉴항목들
urlpatterns = [
    #admin 기본정의 항목
    path('admin/', admin.site.urls),
    path("", main), #공백과 main 함수를 연결
]

