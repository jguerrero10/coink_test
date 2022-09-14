from django.db import models


class UserBasic(models.Model):
    fullname = models.CharField(max_length=180)
    email = models.EmailField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname
