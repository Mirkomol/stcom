# Generated by Django 4.2.6 on 2023-11-07 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stmain', '0002_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
