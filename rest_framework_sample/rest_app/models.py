from django.db import models

class EmployeeRegistration(models.Model):
    employeeid=models.IntegerField(primary_key=True,unique=False)
    empname=models.CharField(max_length=30)
    empsalary=models.DecimalField(max_digits=6,decimal_places=2)
    empimg=models.ImageField(upload_to='rest_frame_images/',default=False)
