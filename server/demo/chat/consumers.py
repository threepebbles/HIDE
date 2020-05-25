# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import get_object_or_404

import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from hide.views.myfile_views import network_state_check, network_state_modify

from django.contrib.auth.decorators import login_required
from channels.auth import login

from hide.models import NetworkState
from hide.forms import NetworkStateForm
from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.user = self.scope["user"]

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        my_network_state = get_object_or_404(NetworkState, author_id=self.user.id)
        my_network_state.network_state = False
        my_network_state.save()
        print("[server]: client socket is closed")

        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        print("[server]: user id="+str(self.user.id) + " sent message")
        text_data_json = json.loads(text_data)

        my_network_state = network_state_check(self.user)
        network_state_modify(self.user, "True")
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )


    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))