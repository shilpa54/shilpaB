from django.shortcuts import render,redirect
from .views import *
from .forms import *
from .models import *
from django.http import HttpResponse
from django.core.mail import send_mail
from cookingpro.settings import EMAIL_HOST_USER
import uuid
from django.contrib import messages
import os
#
# from django.contrib.auth import authenticate


# Create your views here.
def home(request):
    return render(request,"home.html")
def chefreg(request):
    if request.method=='POST':
        a=chefregform(request.POST)
        if a.is_valid():
            fn=a.cleaned_data['fname']
            un=a.cleaned_data['uname']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phone']
            ps=a.cleaned_data['password']
            cp=a.cleaned_data['cpassword']


            if ps==cp:
                b = chefregmodel(fname=fn, uname=un, email=em, phone=ph, password=ps)
                b.save()
                return redirect(cheflog)
        else:
            return HttpResponse('registration failed')
    return render(request,'chefreg.html')
def cheflog(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            us=a.cleaned_data['uname']
            ps=a.cleaned_data['password']

            b=chefregmodel.objects.all()
            for i in b:
                if us==i.uname and ps==i.password:
                    em=i.email
                    return redirect(chefprofile)
            else:
                return HttpResponse('login failed')
    else:
        return render(request,'cheflog.html')
def chefprofile(request):
    return render(request,"chefprofile.html")
def nfile(request):
    if request.method=='POST':
        a=nform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['nitem']
            de=a.cleaned_data['ndis']
            im=a.cleaned_data['nimage']
            b=nonmodel(nitem=nm,ndis=de,nimage=im)
            b.save()
            return redirect(ndisplay)
        else:
            return HttpResponse("file upload failed")
    else:
        return render(request,"nupload.html")

def vfile(request):
    if request.method=='POST':
        a=vform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['vitem']
            np=a.cleaned_data['vprice']
            de=a.cleaned_data['vdis']
            im=a.cleaned_data['vimage']
            b=vmodel(vitem=nm,vprice=np,vdis=de,vimage=im)
            b.save()
            return HttpResponse("success")
        else:
            return HttpResponse("file upload failed")
    else:
        return render(request,"vegupload.html")


def ndisplay(request):
   x=nonmodel.objects.all()
   li=[]
   item=[]

   des1=[]
   id=[]
   for i in x:
       path=i.nimage
       li.append(str(path).split("/")[-1])
       nm=i.nitem
       item.append(nm)

       dis=i.ndis
       des1.append(dis)
       id1=i.id
       id.append(id1)
   mylist=zip(li,item,des1,id)
   return render(request,'nondisplay.html',{'mylist':mylist})
def nonedit(request,id):
    prod=nonmodel.objects.get(id=id)
    li=str(prod.nimage).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES) !=0:
            if len(prod.nimage) >0:
                os.remove(prod.nimage.path)
            prod.nimage=request.FILES['nimage']
        prod.nitem=request.POST.get('nitem')
        prod.ndescription=request.POST.get('ndis')
        prod.nprice=request.POST.get('nprice')
        prod.save()
        return redirect(ndisplay)
    ##context={'prod':prod}
    return render(request,'nonedit.html',{'prod':prod,'li':li})

def nondelete(request,id):
    prod=nonmodel.objects.get(id=id)
    if len(prod.nimage)>0:
        os.remove(prod.nimage.path)
    prod.delete()
    return redirect(ndisplay)

def vdisplay(request):
   x=vmodel.objects.all()
   li=[]
   item=[]
   price = []
   des1=[]
   for i in x:
       path=i.vimage
       li.append(str(path).split("/")[-1])
       nm=i.vitem
       item.append(nm)
       pri=i.vprice
       price.append(pri)
       dis=i.vdis
       des1.append(dis)
   mylist=zip(li,item,price,des1)
   return render(request,'vegdisplay.html',{'mylist':mylist})

def aboutus(request):
    return render(request,'about.html')
# def contactus(request):
#     return render(request,'contact.html')

def userreg(request):
    if request.method == 'POST':
        a = userregform(request.POST)
        if a.is_valid():
            fn = a.cleaned_data['fullname']
            un = a.cleaned_data['username']
            ps = a.cleaned_data['password']
            cp = a.cleaned_data['cpassword']
            if ps == cp:
                b = userregmodel(fullname=fn, username=un ,password=ps)
                b.save()
                return redirect(userlog)
        else:
            return HttpResponse('registration failed')
    return render(request, 'userreg.html')


def userlog(request):
    if request.method == 'POST':
        a = userlogform(request.POST)
        if a.is_valid():
            us = a.cleaned_data['username']
            psw = a.cleaned_data['password']
            b = userregmodel.objects.all()
            for i in b:
                if us == i.username and psw == i.password:
                    return redirect(chefprofile)
            else:
                return HttpResponse('login failed')
    else:
        return render(request, 'userlog.html')

def contactus(request):
    sub=contactusform()
    if request.method=='POST':
        sub=contactusform(request.POST)
        if sub.is_valid():
            Email=sub.cleaned_data['email']
            Name=sub.cleaned_data['name']
            Message=sub.cleaned_data['message']
            send_mail(str(Name)+'||'+str(Email),Message,EMAIL_HOST_USER,[Email],fail_silently=False)
            return render(request,'contactsend.html')
    return render(request,'contact.html',{'form':sub})




