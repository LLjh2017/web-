from django.db import models

# Create your models here.


class User(models.Model):
    uname = models.CharField(max_length=30)
    upwd = models.CharField(max_length=30)
    uemail = models.EmailField()

    class Meta:
        db_table = "user"

