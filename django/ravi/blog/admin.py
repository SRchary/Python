from django.contrib import admin
from .models import Post as psts

# Register your models he

class PostModalAdmin(admin.ModelAdmin):

    #fields = ( 'title' ,"created_data" , 'update_data')
    pass

admin.site.register(psts ,PostModalAdmin)
