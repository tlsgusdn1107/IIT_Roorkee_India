# Generated by Django 3.1.2 on 2020-10-15 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tailscout_app', '0003_auto_20201014_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='bacteria',
            field=models.CharField(choices=[('B1', 'Bacteria_1'), ('B2', 'Bacteria_2'), ('B2', 'Bacteria_3')], max_length=2),
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('S1', 'Step_1'), ('S2', 'Step_2'), ('S3', 'Step_3')], default='S1', max_length=2),
        ),
    ]
