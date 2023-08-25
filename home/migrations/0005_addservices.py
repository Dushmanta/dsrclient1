# Generated by Django 3.2.3 on 2022-05-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_service_price_ser'),
    ]

    operations = [
        migrations.CreateModel(
            name='addservices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_addserv', models.ImageField(upload_to='media')),
                ('name_serv', models.CharField(max_length=40)),
                ('desc_serv', models.TextField()),
                ('price_serv', models.IntegerField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]