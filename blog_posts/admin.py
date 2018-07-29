from django.contrib import admin

# Register your models here.

from blog_posts.models import Topic,Webpage,AccessRecord

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)