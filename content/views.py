from django.shortcuts import render, redirect, get_object_or_404
import json
from django.http import JsonResponse
from .models import Reply, Feed
# Create your views here.
def reply(request):
    json_object = json.loads(request.body)

    reply = Reply.objects.create(
        feed_id=json_object.get('feedId'),
        content=json_object.get('content'),
    )
    reply.save()
    context = {
        'content': reply.content,

    }

    return JsonResponse(context)

def detail( request, feedid):
    feed = get_object_or_404(Feed, pk=feedid)

    reply = Reply.objects.filter(feed_id=feedid, null=True)
    try:
        session = request.session['feedid']
        context = {
            'feed': feed,
            'reply': reply,
            'session': session,
        }
        return render(request, 'API MAP.html', context)
    except KeyError:
        return redirect('Main.html')