# Generated by Django 4.2.6 on 2023-11-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stfood', '0003_item_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='https://www.greatwall.lk/assets/image/default.png', upload_to='profile_pictures'),
        ),
    ]
