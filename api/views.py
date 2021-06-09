from django.contrib.auth.models import User
from django.http import request
from rest_framework import viewsets, status
from . import permissions
from .serializers import UserSerializer, PublicChatRoomSerializer, PublicChatRoomMessageSerializer
from public_chat.models import PublicChatRoom, PublicChatRoomMessage

  
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = [UserSerializer]

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['update','partial_update','destroy']:
            self.permission_classes = [permissions.IsUser,]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()
   
    def get_queryset(self):
        return User.objects.order_by('-date_joined')
    
class PublicChatRoomViewSet(viewsets.ModelViewSet):
    queryset = PublicChatRoom.objects.all()
    serializer_class = PublicChatRoomSerializer
    permission_classes = [permissions.IsRoomer]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PublicChatRoomMessageViewSet(viewsets.ModelViewSet):
    queryset = PublicChatRoomMessage.objects.all()
    serializer_class = PublicChatRoomMessageSerializer
    #permission_classes = [permissions.IsRoomer]