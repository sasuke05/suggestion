from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    user = models.CharField(max_length=200,default='anonymous')
    madhav_vyas = 'Madhav Vyas'
    nikita_kulkarni = 'Nikita Kulkarni'
    sahilcr = 'CR'
    recipient_choices= (
        ( madhav_vyas,'Madhav Vyas'),
        ( nikita_kulkarni,'Nikita Kulkarni'),
        ( sahilcr,'CR'),
    )
    recipient = models.CharField(max_length=25, choices = recipient_choices, default= madhav_vyas )
   
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    

    def publish(self):
        self.created_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

class Reply(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    postno = models.ForeignKey('suggestion.Post', on_delete=models.CASCADE, related_name='comments')
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text    


    
    
