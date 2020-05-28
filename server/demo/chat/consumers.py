from django.shortcuts import get_object_or_404

import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from hide.views.myfile_views import network_state_check, network_state_modify

from django.contrib.auth.decorators import login_required
from channels.auth import login

from hide.models import NetworkState

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.user

        if self.user.is_authenticated:
            network_state_check(self.user)
            network_state_modify(self.user, "True")
            print("[server]: user id=" + str(self.user.id) + " websocket is connected")
        else:
            print("[server]: Anonymous user websocket is connected")
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        if (self.user.is_authenticated == True):
            print("[server]: user id=" + str(self.user.id) + " websocket is closed")
            my_network_state = get_object_or_404(NetworkState, author_id=self.user.id)
            my_network_state.network_state = False
            my_network_state.save()
        else:
            print("[server]: Anonymous user websocket is closed")

        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        if(self.user.is_authenticated):
            print("[server]: user id="+str(self.user.id) + " sent message")
        else:
            print("[server]: Anonymous user sent message")

        text_data_json = json.loads(text_data)
        file_path = text_data_json["file_path"]
        file_state = text_data_json["file_state"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'file_path': file_path,
                'file_state': file_state
            }
        )


    # Receive message from room group
    def chat_message(self, event):
        file_path = event['file_path']
        file_state = event['file_state']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'file_path': file_path,
            'file_state': file_state
        }))