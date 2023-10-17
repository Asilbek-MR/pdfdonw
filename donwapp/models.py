from django.db import models

# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=70)
    test = models.TextField()
    
    def __str__(self):
        return self.name