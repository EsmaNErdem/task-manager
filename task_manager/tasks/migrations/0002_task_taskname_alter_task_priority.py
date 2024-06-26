# Generated by Django 5.0.3 on 2024-04-04 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='taskName',
            field=models.CharField(default='task', max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[(1, 'Can wait'), (2, 'Important'), (3, 'Get to work')], max_length=10),
        ),
    ]
