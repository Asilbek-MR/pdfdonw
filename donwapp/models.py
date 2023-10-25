from django.db import models

# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=70)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name