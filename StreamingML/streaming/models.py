from django.db import models

# Create your models here.

class Video(models.Model):

    caption = models.CharField(max_length=300)

    video = models.FileField(upload_to='video/%y')

    def __str__(self) -> str:
        return self.caption

class StreamVideo(models.Model):
    video_file = models.FileField(upload_to='streamvideos/')


'''
Video_metadata class is used to save video metadata information
'''
class Video_metadata(models.Model):
    metadata= models.CharField(max_length=300)
    
