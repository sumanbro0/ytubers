# Generated by Django 4.1.3 on 2022-11-10 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiretuber',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
