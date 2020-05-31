from django.shortcuts import get_object_or_404

import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from hide.views.myfile_views import network_state_check, network_state_modify

from channels.generic.websocket import WebsocketConsumer

from hide.models import NetworkState
from django_user_agents.utils import get_user_agent

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.room_name = str(self.user)
        self.room_group_name = 'chat_%s' % str(self.user)

        # print(self.scope)
        self.headers = dict(self.scope["headers"])
        self.user_agent = self.headers[b'user-agent'].decode("utf-8")

        # print(self.user_agent)
        if self.user.is_authenticated:
            print("user=" + str(self.user) + " websocket is connected")
        else:
            print("Anonymous user websocket is connected")


        if "Windows" in self.user_agent:
            print("windows PC websocket is connected")

            if self.user.is_authenticated:
                network_state_check(self.user)
                network_state_modify(self.user, "True")
        else:
            print("mobile websocket is disconnected")


        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        if (self.user.is_authenticated == True):
            print("user=" + str(self.user) + " websocket is closed")
        else:
            print("Anonymous user websocket is closed")


        if "Windows" in self.user_agent:
            print("windows PC websocket is disconnected")

            if self.user.is_authenticated:
                my_network_state = get_object_or_404(NetworkState, author_id=self.user.id)
                my_network_state.network_state = False
                my_network_state.save()
        else:
            print("mobile websocket is disconnected")

        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        if(self.user.is_authenticated):
            print("user="+str(self.user) + " sent message")
        else:
            print("Anonymous user sent message")

        if "Windows" in self.user_agent:
            print("windows PC sent message")
        else:
            print("mobile sent message")

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