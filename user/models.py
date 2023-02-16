from django.db import models
# Create your models here.
class contactus(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=50)
    Mobile=models.CharField(max_length=12)
    Message=models.TextField()
    def __str__(self):
        return self.Name


class slider(models.Model):
    shead=models.CharField(max_length=300)
    ssubject=models.CharField(max_length=300)
    sdes=models.TextField()
    spic=models.ImageField(upload_to='static/slider/',default="")
def __str__(self):
        return self.shead

class igallery(models.Model):
    gname=models.CharField(max_length=400)
    gpic=models.ImageField(upload_to='static/',default="")
    def __str__(self):
        return self.gname

class iblog(models.Model):
    bname=models.CharField(max_length=40)
    bdes=models.TextField()
    bpicture=models.ImageField(upload_to='static/blogs',null=True)
    bdate=models.DateField()
    def __str__(self):
        return self.bname

class imembership(models.Model):
    mname=models.CharField(max_length=50)
    mcode=models.IntegerField()
    mcity=models.CharField(max_length=50)
    memail=models.CharField(max_length=50)
    mbank=models.IntegerField()
    mcompany=models.CharField(max_length=50)
    madd=models.TextField(max_length=200)

class city(models.Model):
    cityn=models.CharField(max_length=50)


class idonate(models.Model):
    damount=models.IntegerField()
    dfname=models.CharField(max_length=15)
    dlname=models.CharField(max_length=15)
    demail=models.CharField(max_length=15)
    dphone=models.IntegerField()
    dcountry=models.CharField(max_length=50)
    dadd=models.TextField()
    dstate=models.CharField(max_length=50)
    dcode=models.IntegerField()
    doccu=models.CharField(max_length=30)

class icountry(models.Model):
    countryd=models.CharField(max_length=30)

class istate(models.Model):
    statei=models.CharField(max_length=100)

class vgallery(models.Model):
    vlink=models.TextField()
    vdes=models.TextField()
    vtitle=models.CharField(max_length=50)
    vdate=models.DateField()