from django.db import models
# Creating models 
class Post(models.Model):
    # Default behaviour - Django creates primary keys for you
    # Placed the field in-between my body and date fields
    title = models.CharField(max_length=140)
    body = models.TextField()
    # added a parameter called default 
    signature = models.CharField(max_length=140, default="Yonela Mica")
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title