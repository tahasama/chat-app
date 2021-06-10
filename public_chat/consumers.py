import json

from channels.generic.websocket import  WebsocketConsumer, AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from asgiref.sync import async_to_sync
import asyncio
from channels.consumer import AsyncConsumer
from django.utils import timezone

from .models import PublicChatRoomMessage, PublicChatRoom

from django.shortcuts import render, redirect, get_object_or_404
from .models import PublicChatRoom


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_%s' % self.id
        # join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # accept connection
        await self.accept()

    async def disconnect(self, close_code):
        # leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        now = timezone.now()
        #save the message
        await self.save_message(message)
        # send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user.username,
                'datetime': now.isoformat(),
            }
        )

    # receive message from room group
    async def chat_message(self, event):
        # send message to WebSocket
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def save_message(self,message):
        course = get_object_or_404(PublicChatRoom,id=self.id)
        messages = PublicChatRoomMessage.objects.create(user=self.scope['user'], content=message,room=course)
        return messages

        

    