# Generated by Django 2.1 on 2019-02-18 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_image'),
        ),
    ]