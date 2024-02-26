import os

from django.contrib.auth.models import User
from .models import ChatUser, ChatRoom, Message
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .serializers import ChatUserSerializer, ChatRoomSerializer, MessageSerializer, UserSerializer


class AllUsersView(generics.ListAPIView):
    queryset = User.objects.order_by('-last_login')
    serializer_class = UserSerializer


class AllChatUsersView(generics.ListAPIView):
    queryset = ChatUser.objects.order_by('-user__last_login')
    serializer_class = ChatUserSerializer


class ChangeChatUserView(generics.UpdateAPIView):
    queryset = ChatUser.objects.all()
    serializer_class = ChatUserSerializer

    def put(self, request, pk):
        chat_user = self.get_object()
        user = User.objects.get(pk=chat_user.user.pk)
        print(request.data)
        user.username = request.data['user']['username']
        user.save()
        print(request.data['avatar'])
        os.system(f"copy {request.data['avatar']} media/{os.path.basename(request.data['avatar'])}")
        chat_user.avatar = request.data['avatar']
        chat_user.avatar = f"{os.path.basename(request.data['avatar'])}"
        chat_user.save()
        return Response({'message': 'Profile is changed'})


class AllChatRoomsView(generics.ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


class ChatRoomView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

    def put(self, request, pk):
        room = self.get_object()
        guests = request.data['users']
        room.users.set(guests)
        room.save()
        return Response({'message': 'Some guests are changed'})


class AllMessagesView(generics.ListCreateAPIView):
    queryset = Message.objects.order_by('-creation_date')
    serializer_class = MessageSerializer
