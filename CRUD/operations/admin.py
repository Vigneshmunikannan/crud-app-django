from django.contrib import admin
from .models import Student



# giving access to admin for Student data base
admin.site.register(Student)
