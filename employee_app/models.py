from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=500, unique=True)
    mobile = models.CharField(max_length=15)
    department = models.CharField(choices=(("Development", "Development"),
                                            ("Testing", "Testing"), ("HR", "HR")), max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class EmployeeAttendanace(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    is_present = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
