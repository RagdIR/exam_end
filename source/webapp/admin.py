from django.contrib import admin

from webapp.models import Users, Friends, Message


admin.site.register(Users)
admin.site.register(Friends)
admin.site.register(Message)