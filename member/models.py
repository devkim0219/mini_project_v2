from django.db import models

# Create your models here.
class Member(models.Model):
    objects = models.Manager()
    mem_id = models.CharField(primary_key=True, max_length=20)
    mem_pw = models.CharField(max_length=200)
    mem_name = models.CharField(max_length=20)
    mem_tel = models.CharField(max_length=20)
    mem_email = models.CharField(max_length=40)
    mem_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mem_name