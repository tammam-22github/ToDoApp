from django.db import models

# Create your models here.


class Tasks(models.Model):
    title=models.CharField(max_length=50)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['created']
        indexes=[
            models.Index(fields=['title','created']),
            ]

    def __str__(self):
        return self.title
