from django.db import models

# Create your models here.
role_cho = [("admin", "admin"), ("SuperAdmin", "SuperAdmin"), ("User", "User")]

class Pengguna(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    roles = models.CharField(choices=role_cho, max_length=20)
