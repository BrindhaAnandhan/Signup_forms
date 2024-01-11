from django.db import models

# Create your models here.
class SignUp(models.Model):
    UserName = models.CharField(max_length = 100, primary_key = True)
    Email = models.EmailField()
    Password = models.CharField(max_length = 10)
    CPassword = models.CharField(max_length = 10)
    
    def __str__(self) -> str:
        return self.UserName