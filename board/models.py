from django.db import models

# Create your models here.
class Board(models.Model):
    objects = models.Manager()
    brd_no = models.AutoField(primary_key=True)
    brd_title = models.CharField(max_length=150)
    brd_content = models.TextField()
    brd_writer = models.CharField(max_length=20)
    brd_hit = models.IntegerField()
    brd_date = models.DateTimeField(auto_now_add=True)
    brd_img = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.brd_title