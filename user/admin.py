from django.contrib import admin
from .models import *
# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ("Name","Email","Mobile","Message",)

admin.site.register(contactus,contactusAdmin)

class igalleryAdmin(admin.ModelAdmin):
    list_display=('gname','gpic')

admin.site.register(igallery,igalleryAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display=('id','shead','ssubject','sdes','spic')

admin.site.register(slider,sliderAdmin)

class iblogAdmin(admin.ModelAdmin):
    list_display =('bname','bdes','bpicture','bdate','id')

admin.site.register(iblog,iblogAdmin)

class imembershipAdmin(admin.ModelAdmin):
    list_display =('mname','mcode','mcity','memail','mbank','mcompany','madd','id')

admin.site.register(imembership,imembershipAdmin)

class cityAdmin(admin.ModelAdmin):
    list_display = ('cityn','id')

admin.site.register(city,cityAdmin)

class idonateAdmin(admin.ModelAdmin):
    list_display = ('damount','dfname','dlname','demail','dphone','dcountry','dadd','dstate','dcode','id')

admin.site.register(idonate,idonateAdmin)

class icountryAdmin(admin.ModelAdmin):
    list_display = ('countryd','id')

admin.site.register(icountry,icountryAdmin)

class istateAdmin(admin.ModelAdmin):
    list_display = ('statei','id')

admin.site.register(istate,istateAdmin)

class vgalleryAdmin(admin.ModelAdmin):
    list_display = ('vlink','vdes','vtitle','vdate','id')

admin.site.register(vgallery,vgalleryAdmin)