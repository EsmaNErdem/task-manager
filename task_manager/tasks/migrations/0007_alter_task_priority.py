# Generated by Django 5.0.3 on 2024-04-10 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(choices=[(1, 'Can wait'), (2, 'Important'), (3, 'Get to work')], default=1),
        ),
    ]
