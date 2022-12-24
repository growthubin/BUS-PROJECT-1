from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed, Reply
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
        return render(request, "Bus project//Main.html")


class Sub1(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        print("겟으로 호출")
        return render(request, "Bus project//API MAP.html")

    def post(self, request):
        print("포스트로 호출")
        return render(request, "Bus project//API MAP.html")


class Sub2(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        all_feed = Feed.objects.all()  # 모든 관광장소 불러오기

        content = {'all_feed': all_feed, }
        print("겟으로 호출")
        return render(request, "Bus project//Locating_only.html", context=content)

    def post(self, request):
        print("포스트로 호출")
        return render(request, "Bus project//Locating_only.html")


class searchResult(APIView):

    def get(self, request):

        query = None
        feeds1 = None
        reply_list = []

        if 'kw' in request.GET:
            query = request.GET.get('kw')
            feeds1 = Feed.objects.all().filter(
                Q(name__icontains=query)
            )

            for feed in feeds1:
                reply_object_list = Reply.objects.filter(feed_id=feed.id)  # 해당 feed id에 해당하는 댓글 리스트 찾기
                reply_list = []

                for reply in reply_object_list:
                    reply_list.append(dict(reply_content=reply.content))

                print(reply_list)
                # nickname=user.nickname)) 추후 익명 추가

            content = {'query': query, 'feeds1': feeds1, 'reply_list': reply_list}
            return render(request, "Bus project//API MAP.html", context=content)
