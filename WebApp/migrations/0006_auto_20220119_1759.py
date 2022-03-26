# Generated by Django 3.2.7 on 2022-01-19 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0005_devices_interfaces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interfaces',
            name='port',
            field=models.IntegerField(choices=[(0, 'Port 0'), (1, 'Port 1')], default=0),
        ),
        migrations.AlterField(
            model_name='interfaces',
            name='slot',
            field=models.IntegerField(choices=[(0, 'Slot 0'), (1, 'Slot 1')], default=0),
        ),
        migrations.AlterField(
            model_name='interfaces',
            name='status',
            field=models.CharField(choices=[('u', 'Up'), ('d', 'Down')], default='u', max_length=4),
        ),
        migrations.AlterField(
            model_name='interfaces',
            name='type',
            field=models.CharField(choices=[('Fast', 'FastEthernet'), ('Gig', 'GigabitEthernet')], default='Fast', max_length=20),
        ),
    ]
