# Generated by Django 2.2.17 on 2021-01-04 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_subtask'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='subtasks',
            field=models.ManyToManyField(blank=True, to='dashboard.SubTask'),
        ),
    ]