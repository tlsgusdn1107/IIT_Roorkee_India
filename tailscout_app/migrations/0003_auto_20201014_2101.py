# Generated by Django 3.1 on 2020-10-14 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tailscout_app', '0002_auto_20201014_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('S1', 'Step_1'), ('S2', 'Step_2'), ('S3', 'Step_3')], max_length=2),
        ),
    ]
