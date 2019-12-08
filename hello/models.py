from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Posts(models.Model):

    Title = models.CharField(max_length=100)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Context = models.TextField()
    Date_Posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Title
