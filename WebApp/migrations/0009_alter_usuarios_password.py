# Generated by Django 3.2.7 on 2022-03-25 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0008_usuarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='password',
            field=models.CharField(max_length=15),
        ),
    ]
