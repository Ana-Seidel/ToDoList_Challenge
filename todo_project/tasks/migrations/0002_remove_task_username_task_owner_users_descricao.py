# Generated by Django 5.0.7 on 2024-08-02 21:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='username',
        ),
        migrations.AddField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.users'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='descricao',
            field=models.TextField(blank=True),
        ),
    ]
