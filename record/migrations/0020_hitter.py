# Generated by Django 2.2.5 on 2019-12-13 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0019_delete_hitter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hitter',
            fields=[
                ('h_index', models.AutoField(primary_key=True, serialize=False)),
                ('h_no', models.IntegerField()),
                ('h_name', models.CharField(max_length=50)),
                ('h_team', models.CharField(max_length=50)),
                ('h_avg', models.CharField(max_length=20)),
                ('h_game', models.CharField(max_length=20)),
                ('h_pa', models.CharField(max_length=20)),
                ('h_ab', models.CharField(max_length=20)),
                ('h_r', models.CharField(max_length=20)),
                ('h_h', models.CharField(max_length=20)),
                ('h_2b', models.CharField(max_length=20)),
                ('h_3b', models.CharField(max_length=20)),
                ('h_hr', models.CharField(max_length=20)),
                ('h_tb', models.CharField(max_length=20)),
                ('h_rbi', models.CharField(max_length=20)),
                ('h_sac', models.CharField(max_length=20)),
                ('h_sf', models.CharField(max_length=20)),
            ],
        ),
    ]
