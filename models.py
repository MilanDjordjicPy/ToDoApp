from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length= 25, null= True, blank = True)
    description = models.TextField(null = True, blank = True, max_length = 64)
    complete = models.BooleanField(default= False)
    date_created = models.DateTimeField(auto_now_add=True)
    #date_expiring = models.DateTimeField(auto_created = True)
    #date_completed = models.DateTimeField(blank = True, null = True)
    def __str__(self):
        return str(self.title)
    class Meta:
        ordering = ['complete']