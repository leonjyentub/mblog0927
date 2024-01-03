from django.contrib import admin
from mytest.models import Post, Mood,Profile
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname','message','del_pass', 'pub_time', 'enabled')
    
admin.site.register(Profile)
admin.site.register(Post, PostAdmin)
admin.site.register(Mood)