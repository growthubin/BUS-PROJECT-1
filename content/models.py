from django.db import models

# Create your models here.
class Feed(models.Model):
    name = models.TextField()
    image = models.TextField()
    location = models.TextField()
    explain = models.TextField()
    conv = models.TextField()
    detail = models.TextField(default='aa')
    address = models.TextField(default='aa')

class Reply(models.Model):
    content = models.CharField(max_length=255)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE,)
