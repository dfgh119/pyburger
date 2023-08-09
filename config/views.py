#주문을 처리하는 직원

from django.http import HttpResponse

def main(request): # main 함수 정의
    return HttpResponse("안녕하세요 pyburger입니다.")
