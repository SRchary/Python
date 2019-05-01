from django.contrib import admin

from .models import AuthorModel 
# Register your models here.

class AuthorModel_admin(admin.ModelAdmin):
    fields =[
        "author_name",
        "author_phone",
        "author_email",
        "author_address",
        "dob",
        "created_on",
        "updated_on",


        ]
    readonly_fields =["created_on","updated_on"]

    class meta:
        model = AuthorModel

admin.site.register(AuthorModel ,AuthorModel_admin)
