from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:300]
     
    def pub_date_pretty(self):
        return self.created_at.strftime('%b %e %Y')
   

 
    
