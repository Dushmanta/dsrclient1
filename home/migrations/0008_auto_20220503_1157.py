# Generated by Django 3.2.3 on 2022-05-03 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_repair_centre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repair_centre',
            old_name='desc_serv',
            new_name='desc_rer',
        ),
        migrations.RemoveField(
            model_name='repair_centre',
            name='se',
        ),
    ]
