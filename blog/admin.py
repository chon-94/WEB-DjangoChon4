from django.contrib import admin
from .models import Post,User,Script

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Script)