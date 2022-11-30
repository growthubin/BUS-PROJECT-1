
from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        print("겟으로 호출")
        return render(request, "Bus project//Main.html")

    def post(self, request):
        print("포스트로 호출")
        return render(request,"Bus project//Main.html")

class Sub1(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        print("겟으로 호출")
        return render(request, "Bus project//API MAP.html")

    def post(self, request):
        print("포스트로 호출")
        return render(request,"Bus project//API MAP.html")

class Sub2(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        print("겟으로 호출")
        return render(request, "Bus project//example.html")

    def post(self, request):
        print("포스트로 호출")
        return render(request,"Bus project//example.html")