from django.contrib.auth.models import User
from rest_framework import serializers
from public_chat.models import PublicChatRoom, PublicChatRoomMessage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','last_name']
        #fields = ['url', 'username']


class PublicChatRoomMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicChatRoomMessage
        fields = ['user','room','content', 'time_stamp']  


class PublicChatRoomSerializer(serializers.ModelSerializer):
    chatroom_messages = PublicChatRoomMessageSerializer(many=True,required=False)
    owner = serializers.ReadOnlyField(source='owner.username') # so that perform_create works
    class Meta:
        model = PublicChatRoom
        fields = ['id','title', 'owner','joiners','chatroom_messages']


        

