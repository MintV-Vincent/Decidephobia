# Generated by Django 5.0.2 on 2024-03-21 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='profile_pictures/default.jpg', upload_to='profile_pictures/'),
        ),
    ]
