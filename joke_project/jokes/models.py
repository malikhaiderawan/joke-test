from django.db import models
from django.contrib.auth.models import User

class Joke(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text
