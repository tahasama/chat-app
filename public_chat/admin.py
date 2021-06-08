from django.contrib import admin
from django.core.cache.backends.base import CacheKeyWarning
# from django.core.paginator import Paginator
# from django.core.cache import cache
# from django.db import models

from .models import PublicChatRoom, PublicChatRoomMessage


class PublicChatRoomAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    search_fields = ['id','title']
    list_filter = ['id']

    class Meta:
        model = PublicChatRoom

admin.site.register(PublicChatRoom, PublicChatRoomAdmin)

class PublicChatRoomMessageAdmin(admin.ModelAdmin):
    list_display = ['room','user','time_stamp']
    search_fields = ['room__title','user__username','content']
    list_filter = ['room','user','time_stamp']

    show_full_result_count = False

    class Meta:
        model = PublicChatRoomMessage

admin.site.register(PublicChatRoomMessage, PublicChatRoomMessageAdmin)
