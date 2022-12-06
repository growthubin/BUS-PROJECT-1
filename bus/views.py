
from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed
from django.db.models import Q
from rest_framework.response import Response


class Sub(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        print("겟으로 호출")

        feed_list = Feed.objects.order_by("?")[:9]
        print(feed_list)
        return render(request, "Bus project//Main.html", context=dict(feeds=feed_list))

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




class searchResult(APIView):

    def get(self,request):

        query=None
        feeds1=None

        if 'kw' in request.GET:
            query = request.GET.get('kw')
            feeds1 = Feed.objects.all().filter(
                Q(name__icontains=query)
            )
        return render(request,"Bus project//API MAP.html",{'query':query,'feeds1':feeds1})
