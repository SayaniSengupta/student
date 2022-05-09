from django.db import models

# Create your models here.
class stu (models.Model):
    regNo = models.TextField(unique=True)
    name = models.TextField()
    email = models.TextField()
    mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)