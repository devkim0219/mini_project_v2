# Generated by Django 2.2.5 on 2019-12-12 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0010_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pitcher',
            fields=[
                ('p_index', models.AutoField(primary_key=True, serialize=False)),
                ('p_no', models.IntegerField()),
                ('p_name', models.CharField(max_length=50)),
                ('p_team', models.CharField(max_length=50)),
                ('p_era', models.CharField(max_length=20)),
                ('p_game', models.CharField(max_length=20)),
                ('p_win', models.CharField(max_length=20)),
                ('p_lose', models.CharField(max_length=20)),
                ('p_sv', models.CharField(max_length=20)),
                ('p_hld', models.CharField(max_length=20)),
                ('p_wpct', models.CharField(max_length=20)),
                ('p_ip', models.CharField(max_length=20)),
                ('p_h', models.CharField(max_length=20)),
                ('p_hr', models.CharField(max_length=20)),
                ('p_bb', models.CharField(max_length=20)),
                ('p_hbp', models.CharField(max_length=20)),
                ('p_so', models.CharField(max_length=20)),
                ('p_r', models.CharField(max_length=20)),
                ('p_er', models.CharField(max_length=20)),
                ('p_whip', models.CharField(max_length=20)),
            ],
        ),
    ]
