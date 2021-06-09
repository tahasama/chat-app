from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# replaces Course
class PublicChatRoom(models.Model): 
    title = models.CharField(max_length=100, unique=True, blank=False)
    owner = models.ForeignKey(User,related_name='chatrooms_created',on_delete=models.CASCADE)
    joiners = models.ManyToManyField(User, blank=True,related_name='chatrooms_joined', help_text='users who are connected to the chat')

    def __str__(self):
        return self.title

# class PublicChatRoomMessageManager(models.Manager):
#     def by_room(self, room):
#         return PublicChatRoomMessage.objects.filter(room=room).order_by("-time_stamp")

# replaces message
class PublicChatRoomMessage(models.Model):
    user = models.ForeignKey(User,related_name='author_messages', on_delete=models.CASCADE)
    room = models.ForeignKey(PublicChatRoom,blank=True, null=True, related_name='chatroom_messages', on_delete=models.CASCADE)
    #time_stamp = models.models.DateTimeField(auto_now=False, auto_now_add=False)
    time_stamp = models.DateTimeField(default=timezone.now)
    content = models.TextField(unique=False, blank=True)

    # room_objects = PublicChatRoomMessageManager()
    objects = models.Manager()

    def __str__(self):
        return self.content
