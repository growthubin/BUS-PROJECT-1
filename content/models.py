from django.db import models

# Create your models here.
class Feed(models.Model):
    name = models.TextField(null=True)
    image = models.TextField()
    location = models.TextField()
    convenience = models.TextField(null=True)
    explain = models.TextField()

class Reply(models.Model):
    content = models.CharField(max_length=255)
    feed = models.ForeignKey(Feed, null=True, blank=True, on_delete=models.CASCADE,)

