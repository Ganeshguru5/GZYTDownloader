from os import name
from django.urls import path,include
from . import views
app_name='gz'
urlpatterns = [
    path('',views.home,name='homepage'),
    path('download/',views.download,name='downloadpage'),
    path('makedownload/<resolution>',views.downloaddone,name='donedownload')
]