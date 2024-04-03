from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    email = models.EmailField(null='True')
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.subject
