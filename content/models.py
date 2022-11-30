from django.db import models
3
# Create your models here.
class Feed(models.Model):
    name = models.TextField()
    image = models.TextField()
    location = models.TextField()
    convenience = models.TextField(default=0)
    explain = models.TextField()

class Reply(models.Model):
    content = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)

