from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
  movie_id = models.IntegerField()
  score = models.IntegerField()
  title = models.CharField(max_length=128)
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

  def __str__(self):
    return str(self.movie_id) + ' - ' + str(self.score)
