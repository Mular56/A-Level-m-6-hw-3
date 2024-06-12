from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Comments(models.Model):
    START = 'start'
    MIDDLE = 'middle'
    FINISH = 'finish'
    UPDATED_START = 'updated_start'  

    COMMENT_TYPES = [
        (START, 'Start'),
        (MIDDLE, 'Middle'),
        (FINISH, 'Finish'),
        (UPDATED_START, 'Updated Start'),  
    ]

    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment_type = models.CharField(max_length=220, choices=COMMENT_TYPES, default=START)

    def __str__(self):
        return self.text
    
    def save(self):
        self.created_at = timezone.now() - timezone.timedelta(days=365)
        return super().save()

