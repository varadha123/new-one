# Generated by Django 5.0.3 on 2024-03-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.TextField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='status',
            field=models.TextField(max_length=15, null=True),
        ),
    ]
