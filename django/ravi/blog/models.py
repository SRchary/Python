from django.db import models
import datetime

# Create your models here.
post_status = (
    ("publish" , "Publish"),
    ("private" , "Private"),
    ("draft" , "Draft"),

)

class Post(models.Model):

    title  = models.CharField(max_length=250   ,default=None)
    message  = models.TextField(default=None)
    publish_status = models.CharField( max_length=50, default='publish',choices= post_status )
    is_active = models.BooleanField(default=True ,verbose_name=  "Activate")
    created_data = models.DateTimeField(auto_now_add=True  )
    update_data = models.DateTimeField(auto_now=True )

    class Meta:
        verbose_name = "All Posts"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
