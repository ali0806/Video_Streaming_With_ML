from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views as stream_views
from django.conf.urls.static import static

urlpatterns = [
    path('live/',stream_views.synchronize_frame,name='web_feed'),
    path('streaming/',stream_views.index,name='streaming'),
] 
