from django.shortcuts import  render , redirect
import json
from django.http import JsonResponse
from .models import Reply

# Create your views here.
def reply(request):
    jsonObject = json.loads(request.body)
    reply = Reply.objects.create(
        feed_id=jsonObject.get('feedid'),
        content=jsonObject.get('content'))
    reply.save()
    context = {
        'name': reply.feed.name,
        'content': reply.content,

    }

    return JsonResponse(context);

def detail(request,feedid):
    feed = get_object_or_404(Feed,pk=feedid)
    reply = Reply.objects.filter(feed_id=feedid)
    try:
        session = request.session['feedid']
        context = {
            'feed':feed,
            'reply':reply
        }
        return render(request, 'API MAP.html', context)
    except KeyError:
        return redirect('main')