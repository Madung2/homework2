
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth import login, authenticate

def sum_numbers(num1, num2):
    return num1+num2

# Create your views here.
class UserView(APIView):
    # permission_class = [permissions.AllowAny]  # 모든 사람 통과
    permission_class = [permissions.IsAuthenticated]  # 인증된 사람만
    # permission_class = [permissions.IsAdminUser]

    def get(self, request):
        '''
        로그인한 사용자의 정보를 데이터에 포함시켜서 리턴해주는 메소드입니다.
        '''
        # 사용자 정보 조회
        # try:
        #     Model.objects.get(id=obj id)
        # except Model.DoesNotExist:
        #     return Response("존재하지 않는 오브젝트입니다.")
        return Response({"message": "값입니다"})

    def post(self, request):
        # 회원가입
        return Response({"message": "post method!!"})

    def put(self, request):
        # 회원정보 수정
        return Response({"message": "put method!!"})

    def delete(self, request):
        # 회원 탈퇴
        return Response({"message": "delete method!!"})


class UserAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    #로그인
    def post(self,request):

        user = authenticate(request, **request.data) #**request.data 대신에 username=username, password=password 가능
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다"})
        login(request, user)

        return Response({"message": "login success!"})

