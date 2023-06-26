from django.db import models

# Create your models here.

class Subscribe(models.Model):
    email = models.CharField(max_length=128)




class Contact(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=128)
    message = models.TextField()

    def __str__(self):
        return self.name