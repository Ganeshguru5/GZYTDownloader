from django.conf.urls import url
from django.shortcuts import redirect, render
from pytube import YouTube
import os
# Create your views here.
def home(request):
    return render(request,'home.html')

def download(request):
    global url
    url=request.GET.get('url') #1               #2
    yt=YouTube(url)  
    video=[]
    video=yt.streams.filter(progressive=True).all() 
    print("----video----")
    print(video)     
    embed_link=url.replace('.be','be.com/embed')
    embed_link1=embed_link.replace('youtube','www.youtube')
    print("----embed_link----")
    print(embed_link1)
    Title=yt.title
    context={
        'video':video,
        'embed':embed_link1,
        'title':Title
    }
    
    return render(request,'videopage.html',context)

def downloaddone(request,resolution):
    global url
    homedir=os.path.expanduser('~')
    dirs=homedir+'/Downloads'
    if request.method == 'POST':
        if (resolution=='144p' and YouTube(url).streams.get_by_resolution(resolution) == None):
            YouTube(url).streams.get_by_itag(17).download(dirs)
            return render(request,'success.html')
        else:
            YouTube(url).streams.get_by_resolution(resolution).download(dirs)
            return render(request,'success.html')
    return render(request,'errorpage.html')
    