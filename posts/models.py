from django.db import models


class Post(models.model):
    text = models.TextField()