from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=40, null=True)
    password = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.name
