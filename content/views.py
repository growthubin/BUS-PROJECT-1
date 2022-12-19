from django.shortcuts import render, redirect, get_object_or_404
import json
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Reply, Feed
# Create your views here.


class GetReply(APIView):
    def post(self, request):
        json_object = json.loads(request.body)
        feed = Feed.objects.get(id=json_object["feedId"])
        reply = Reply.objects.create(
            feed=feed,
            content=json_object.get('content')
        )
        reply.save()

        # 추후 (익명)도 반환
        context = {
            'content': reply.content,
        }
        return JsonResponse(context)  # html에 뿌리기 위한 return

