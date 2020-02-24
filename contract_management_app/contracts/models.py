from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Contract(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    # date_last_modified =
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
