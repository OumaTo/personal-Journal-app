from django.db import models

class journal(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.TextField(max_length=25)
    content = models.TextField()
    
    
    def __str__(self):
        return f"{self.title} on {self.date}"