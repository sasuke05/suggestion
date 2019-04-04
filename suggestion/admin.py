from django.contrib import admin
from django.conf import settings
from .models import Post,Reply
from django.contrib.auth.models import Group
#username shantanu pass f***tc**b
# Register your models here.

admin.site.site_header='admin dashboard'

class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'user', 'recipient', 'created_date',)
    search_fields=['recipient'] 
    def queryset(self):
        rec=settings.AUTH_USER_MODEL
        if rec=='madhav':
            return Post.objects.filter(recipient='Madhav Vyas')
    
        
    
class ReplyAdmin(admin.ModelAdmin):
     list_display=('text','postno','created_date')

admin.site.register(Post,PostAdmin)
admin.site.register(Reply,ReplyAdmin)
admin.site.unregister(Group)

