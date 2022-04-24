from django.contrib import admin
from blog.models import Blog
from signup.models import Address
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Address)
admin.site.register(Blog)