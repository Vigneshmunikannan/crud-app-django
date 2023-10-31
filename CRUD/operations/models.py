from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)  # Adjust max_length as needed
    department = models.TextField()  # Or use models.CharField if department names are short
    year = models.IntegerField()  # Consider adding validation for valid academic years
