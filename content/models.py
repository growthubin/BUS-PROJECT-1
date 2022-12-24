from django.db import models

# Create your models here.
class Feed(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.TextField()
    image = models.TextField()
    location = models.TextField()
    explain = models.TextField()
    conv = models.TextField()
    detail = models.TextField(default='aa')
    address = models.TextField(default='aa')
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)


class Reply(models.Model):
    content = models.CharField(max_length=255)
    feed = models.ForeignKey(Feed, null=True, default='', on_delete=models.CASCADE,)
