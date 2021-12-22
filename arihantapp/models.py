from django.db import models
from django.conf import settings


class MyData(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length= 300, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    userid = models.PositiveIntegerField(default=1)
