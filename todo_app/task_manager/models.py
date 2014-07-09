from django.db import models
from django.contrib.auth.models import User
import datetime 


 

PRIORITY_CHOICES = ( 

  (1, 'Low'), 

  (2, 'Normal'), 

  (3, 'High'), 

) 
VISIBIITY_CHOICES = ( 

  (1, 'Private'), 

  (2, 'Public'),

) 

STATUS_CHOICES = ( 

  (1, 'Completed'), 

  (2, 'Pending'),

) 


class task(models.Model):
    user_name = models.ForeignKey(User)
    title = models.CharField(max_length=250) 
    created_date = models.DateTimeField(default=datetime.datetime.now) 
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2) 
    visibilty = models.IntegerField(choices=VISIBIITY_CHOICES, default=1) 
    status  = models.IntegerField(choices=STATUS_CHOICES, default=2)  
    def __str__(self): 
        return self.title 

    class Meta: 
        ordering = ['-priority','-status' ,'title'] 

# Create your models here.
