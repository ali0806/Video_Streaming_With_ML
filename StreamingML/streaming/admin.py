from django.contrib import admin
from .models import Video,StreamVideo,Video_metadata
# Register your models here.

admin.site.register(Video)
admin.site.register(StreamVideo)
admin.site.register(Video_metadata)