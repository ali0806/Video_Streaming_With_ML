
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Video
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from .forms import Video_form
from .models import Video,StreamVideo
from .camera import *
from django.core.files.storage import FileSystemStorage
from PIL import Image
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

def live_stream(request):
    # Capture video from the camera
    video_capture = cv2.VideoCapture(0)
    video_capture.set(3, 640)
    video_capture.set(4, 480)
    video_capture.set(5, 30)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while True:
        ret, frame = video_capture.read()
        if ret == True:
            out.write(frame)
            cv2.imshow('Live Streaming', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    out.release()
    cv2.destroyAllWindows()

    # Save video to the database
    video_file = open('output.avi', 'rb')
    fs = FileSystemStorage()
    video_file_name = fs.save(video_file.name, video_file)
    video_url = fs.url(video_file_name)
    video = StreamVideo(video_file=video_file_name, title=request.POST['title'], description=request.POST['description'])
    video.save()
    return render(request, 'streaming/video_uploaded.html', {'video_url': video_url})


def gen(camera):

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while True:
        frame = camera.get_frame()
        # video_file = open('output.avi', 'rb')
        # fs = FileSystemStorage()
        # video_file_name = fs.save(video_file.name, video_file)
        # video_url = fs.url(video_file_name)
        # video = StreamVideo(video_file=video_file_name)
        # video.save()
        yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    
    

def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
                    content_type='multipart/x-mixed-replace; boundary=frame')