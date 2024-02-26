from django.urls import path, include
from .views import *

# from api.views import AllUsersView, AllChatUsersView, AllChatRoomsView, AllMessagesView, ChangeChatUserView, ChatRoomView

urlpatterns = [
    path('users', AllUsersView.as_view()),
    path('chatusers/<int:pk>', ChangeChatUserView.as_view()),
    path('chatusers', AllChatUsersView.as_view()),
    path('rooms/<int:pk>', ChatRoomView.as_view()),
    path('rooms', AllChatRoomsView.as_view()),
    path('messages', AllMessagesView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
