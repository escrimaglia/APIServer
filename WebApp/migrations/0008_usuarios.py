# Generated by Django 3.2.7 on 2022-03-25 17:22

from django.db import migrations, models
import django.forms.widgets


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0007_interfaces_unique slot-port'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('usuario', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=15, verbose_name=django.forms.widgets.PasswordInput)),
            ],
        ),
    ]
