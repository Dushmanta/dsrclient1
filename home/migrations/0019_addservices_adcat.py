# Generated by Django 3.2.3 on 2022-05-14 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_addservices_billingdetails_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='addservices',
            name='adcat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.category'),
        ),
    ]