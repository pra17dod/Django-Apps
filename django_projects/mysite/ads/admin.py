from django.contrib import admin
from .models import Ad
# Register your models here.
class PicAdmin(admin.ModelAdmin):
    exclude = ('picture', 'content_type')


# Register the admin class with the associated model
admin.site.register(Ad,PicAdmin)
