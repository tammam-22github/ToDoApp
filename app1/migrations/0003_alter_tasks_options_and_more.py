# Generated by Django 5.0 on 2024-01-28 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_tasks_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['created']},
        ),
        migrations.RemoveIndex(
            model_name='tasks',
            name='app1_tasks_title_032cbe_idx',
        ),
        migrations.AddIndex(
            model_name='tasks',
            index=models.Index(fields=['title', 'created'], name='app1_tasks_title_5cf6e7_idx'),
        ),
    ]
