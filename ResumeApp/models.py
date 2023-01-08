from django.db import models

class ResumeModel(models.Model):
    pic = models.ImageField(upload_to = "images")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    history = models.CharField(max_length=500)
    phone_number = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
    
