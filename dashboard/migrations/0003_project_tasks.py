# Generated by Django 2.2.17 on 2021-01-04 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tasks',
            field=models.ManyToManyField(blank=True, to='dashboard.Task'),
        ),
    ]
