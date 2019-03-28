from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    user = models.CharField(max_length=200,default='anonymous')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        self.created_date = timezone.now()
        self.save()

    
    
