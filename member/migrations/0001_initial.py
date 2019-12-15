# Generated by Django 2.2.5 on 2019-12-12 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('mem_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('mem_pw', models.CharField(max_length=200)),
                ('mem_name', models.CharField(max_length=20)),
                ('mem_tel', models.CharField(max_length=20)),
                ('mem_email', models.CharField(max_length=40)),
                ('mem_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
