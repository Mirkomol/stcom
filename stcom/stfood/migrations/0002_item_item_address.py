# Generated by Django 4.2.6 on 2023-11-02 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stfood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_address',
            field=models.CharField(default='Istanbul/Turkey', max_length=500),
        ),
    ]
