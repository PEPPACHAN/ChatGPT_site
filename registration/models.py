from django.db import models


class Registered_Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username, self.password
