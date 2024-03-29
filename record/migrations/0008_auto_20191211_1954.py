# Generated by Django 2.2.5 on 2019-12-11 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0007_auto_20191211_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='rcd_awaypoint',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='rcd_awayresult',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='rcd_awayteam',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='rcd_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='rcd_etc',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='rcd_gujang',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='rcd_homepoint',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='rcd_homeresult',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='rcd_hometeam',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
