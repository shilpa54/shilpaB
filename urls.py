from django.urls import path
from .views import *
urlpatterns=[
    path("home/",home),
    path('aboutus/',aboutus),
    path('contactus/',contactus),
    path("chefreg/",chefreg),
    path("cheflog/",cheflog),
    path("chefprofile/",chefprofile),
    path('nfile/',nfile),
    path('vfile/',vfile),
    path('vdisplay/',vdisplay),
    path('ndisplay/',ndisplay),
    path('userreg/',userreg),
    path('userlog/',userlog),
    path('nonedit/<int:id>/',nonedit),
    path('nondelete/<int:id>/',nondelete)

    ]