from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
  api_id = models.CharField(max_length=128)
  type = models.CharField(max_length=16, choices=[('song', "Song"), ('movie', "Movie")])
  score = models.IntegerField()
  title = models.CharField(max_length=128)
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

  def __str__(self):
    return "{} {} by user {}".format(self.type, self.api_id, self.author)
