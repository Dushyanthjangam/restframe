# Generated by Django 2.2.4 on 2019-11-28 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeregistration',
            name='empimg',
            field=models.ImageField(default=False, upload_to='rest_frame_images/'),
        ),
    ]