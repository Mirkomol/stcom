# Generated by Django 4.2.6 on 2023-11-06 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stfood', '0004_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='logo.png', upload_to='profile_pictures'),
        ),
    ]