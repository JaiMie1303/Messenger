from django.contrib.auth.models import User
from rest_framework import serializers

from .models import ChatUser, Message, ChatRoom


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ChatUserSerializer(serializers.ModelSerializer):
    name = UserSerializer()

    class Meta:
        model = ChatUser
        fields = ['id', 'user', 'avatar']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'author', 'creation_date', 'room', 'msg']


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'creation_date', 'author', 'users']


class RoomUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'users']