from django.db import models

# Create your models here.
class Record(models.Model):
    objects = models.Manager()
    rcd_no = models.AutoField(primary_key=True)
    rcd_date = models.CharField(max_length=100, null=True)
    rcd_gujang = models.CharField(max_length=50, null=True)
    rcd_awayteam = models.CharField(max_length=50, null=True)
    rcd_awaypoint = models.CharField(max_length=20, null=True)
    rcd_homepoint = models.CharField(max_length=20, null=True)
    rcd_hometeam = models.CharField(max_length=50, null=True)
    rcd_awayresult = models.CharField(max_length=50, null=True)
    rcd_homeresult = models.CharField(max_length=50, null=True)
    rcd_etc = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.rcd_date

class Pitcher(models.Model):
    objects = models.Manager()
    p_index = models.AutoField(primary_key=True)
    p_no    = models.IntegerField()
    p_name  = models.CharField(max_length=50)
    p_team  = models.CharField(max_length=50)
    p_era   = models.CharField(max_length=20)
    p_game  = models.CharField(max_length=20)
    p_win   = models.CharField(max_length=20)
    p_lose  = models.CharField(max_length=20)
    p_sv    = models.CharField(max_length=20)
    p_hld   = models.CharField(max_length=20)
    p_wpct  = models.CharField(max_length=20)
    p_ip    = models.CharField(max_length=20)
    p_h     = models.CharField(max_length=20)
    p_hr    = models.CharField(max_length=20)
    p_bb    = models.CharField(max_length=20)
    p_hbp   = models.CharField(max_length=20)
    p_so    = models.CharField(max_length=20)
    p_r     = models.CharField(max_length=20)
    p_er    = models.CharField(max_length=20)
    p_whip  = models.CharField(max_length=20)

    def __str__(self):
        return(self.p_index)

class Hitter(models.Model):
    objects = models.Manager()
    h_index = models.AutoField(primary_key=True)
    h_no    = models.IntegerField()
    h_name  = models.CharField(max_length=50)
    h_team  = models.CharField(max_length=50)
    h_avg   = models.CharField(max_length=20)
    h_game  = models.CharField(max_length=20)
    h_pa   = models.CharField(max_length=20)
    h_ab  = models.CharField(max_length=20)
    h_r    = models.CharField(max_length=20)
    h_h   = models.CharField(max_length=20)
    h_2b  = models.CharField(max_length=20)
    h_3b    = models.CharField(max_length=20)
    h_hr    = models.CharField(max_length=20)
    h_tb    = models.CharField(max_length=20)
    h_rbi    = models.CharField(max_length=20)
    h_sac   = models.CharField(max_length=20)
    h_sf    = models.CharField(max_length=20)
    
    def __str__(self):
        return(self.h_index)        

class Team(models.Model):
    objects  = models.Manager()
    t_index  = models.AutoField(primary_key=True)     
    t_no     = models.IntegerField()
    t_name   = models.CharField(max_length=30)
    t_game   = models.IntegerField()
    t_win    = models.IntegerField()
    t_lose   = models.IntegerField()
    t_draw   = models.IntegerField()
    t_per    = models.FloatField()
    t_chai   = models.IntegerField()
    t_10     = models.CharField(max_length=30)
    t_cont   = models.CharField(max_length=30)
    t_home   = models.CharField(max_length=30)
    t_away   = models.CharField(max_length=30)
    t_year   = models.CharField(max_length=30)
    
    def __str__(self):
        return(self.t_index)