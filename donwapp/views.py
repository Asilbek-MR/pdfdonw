from django.shortcuts import render, redirect
from pytube import YouTube
from io import BytesIO
from django.http import StreamingHttpResponse
from .models import Feedback
import re
from django.contrib import messages

# Create your views here.



def index(request):
    # global test_url
    # try:
    # youtubeUrl = request.GET.get("video")
    # if youtubeUrl:
    #     test_url = YouTube(youtubeUrl)
    #     options = test_url.streams.filter(progressive=True)
    #     for option in options:
    #         print(option)
    #     print(test_url.title)
    #     test_title = test_url.title
        # videos = test_url.streams.filter(progressive=True)
        # img_url=test_url.thumbnail_url
        # mesage = '++++++++++++++++'
        # except:
            # mesage = 'Enter Valid YouTube Video URL!'
            # return templates.TemplateResponse("about.html" ,{"request":request, "mesage":mesage})
            #{"request":request, "mesage":mesage,"videos":videos,"test_title":test_title,"img_url":img_url}
        # context = {
        #     "test_url": test_url,
        #     "test_title":test_title
        # }
    return render(request, 'index.html')

def show(request):
    global test_url
    video = request.GET.get('video')
    try:
        re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", video)
        test_url = YouTube(video)
        options = test_url.title
    # except RegexMatchError:
    #     return render(request, 'done.html')
    except Exception:
        return render(request, 'done.html')
        
    if video:
        test_url = YouTube(video)
        options = test_url.streams.filter(progressive=True)
        test_title = test_url.title
        img_url=test_url.thumbnail_url
    
        context = {
            "options":options,
            "test_title": test_title,
            "img_url":img_url,
            "videos": True
        }
    if request.method == "POST":
        download = request.POST.get('download')
        buffer = BytesIO()
        down = test_url.streams.get_by_resolution(download)
        down.stream_to_buffer(buffer)
        buffer.seek(0)
        headers = {
                "Content-Disposition": f'attachment; filename="{test_url.title}.mp4"'
            }
        
        return StreamingHttpResponse(buffer, content_type='video/mp4', headers=headers)
    return render(request, 'about.html', context=context)

def done(request):
    return render(request, 'done.html')

def feedback(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    text = request.POST.get('message')
    Feedback.objects.create(name=name, email=email, subject=subject, text=text)
    return render(request, 'feedback.html')


