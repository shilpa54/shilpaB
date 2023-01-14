from django import forms
class chefregform(forms.Form):
    fname=forms.CharField(max_length=20)
    uname=forms.CharField(max_length=20)
    email=forms.EmailField()
    phone=forms.IntegerField()
    password=forms.CharField(max_length=20)
    cpassword=forms.CharField(max_length=20)
class logform(forms.Form):
    uname=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)
class nform(forms.Form):
    nitem=forms.CharField(max_length=20)
    ndis=forms.CharField(max_length=5000)
    nimage=forms.FileField()
class vform(forms.Form):
    vitem=forms.CharField(max_length=20)
    vprice=forms.IntegerField()
    vdis=forms.CharField(max_length=20)
    vimage=forms.FileField()

class userregform(forms.Form):
    fullname=forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)
    cpassword = forms.CharField(max_length=20)
class userlogform(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)

class contactusform(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    message=forms.CharField(max_length=500,
                            widget=forms.Textarea(attrs={'rows':3,'col':30}))

