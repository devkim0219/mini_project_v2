# Generated by Django 2.2.5 on 2019-12-13 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0017_hitter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hitter',
            old_name='p_rbi',
            new_name='h_rbi',
        ),
        migrations.RenameField(
            model_name='hitter',
            old_name='p_sac',
            new_name='h_sac',
        ),
        migrations.RenameField(
            model_name='hitter',
            old_name='p_sf',
            new_name='h_sf',
        ),
    ]
