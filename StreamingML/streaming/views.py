
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Video
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
from .multiprocessing_ import *
from .forms import Video_form
from .models import Video,StreamVideo
from .camera import *
from django.core.files.storage import FileSystemStorage


# # Create your views here.


def index(request):
    videos= Video.objects.all()

    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('streaming')

    else:
        form = Video_form()


    return render(request,'streaming/streaming.html',{"forms":form,"all":videos})


def synchronize_frame(request):
    return StreamingHttpResponse(grid(),
                     content_type='multipart/x-mixed-replace; boundary=frame')

