from django.db import models
import uuid
from datetime import datetime
# Create your models here.




class MovieRatings(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   
    name = models.CharField(max_length=255, blank=True,null=True)
    rating = models.CharField(max_length=255, blank=True,null=True)
    description = models.CharField(max_length=255, blank=True,null=True)
    
    created_at=models.DateTimeField(blank=True)
    updated_at=models.DateTimeField(blank=True)
    

    
    def save(self, *args, **kwargs):

        current_time = datetime.now()

        if not self.created_at:
            self.created_at = current_time

        self.updated_at = current_time

        super(MovieRatings, self).save(*args, **kwargs)
        return self
