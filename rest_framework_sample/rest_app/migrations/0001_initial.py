# Generated by Django 2.2.4 on 2019-11-28 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeRegistration',
            fields=[
                ('employeeid', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=30)),
                ('empsalary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('empimg', models.ImageField(default=False, upload_to='rest_frame_images')),
            ],
        ),
    ]
