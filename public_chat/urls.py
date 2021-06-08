from django.urls import path

from . import views

urlpatterns = [
    path('register/',views.RegistrationView.as_view(),name='registration'),
    #path('UserJoinChatroom/',views.UserJoinChatroomView.as_view(),name='UserJoinChatroom'),
    path('',views.UsersListView.as_view(),name='UsersListView'),
    path('CreateRoomView/',views.CreateRoomView.as_view(),name='CreateRoomView'),
    path('JoinerRoomDetail/<pk>/',views.JoinerRoomDetailView.as_view(),name='JoinerRoomDetail'),
    path('JoinerRoomDetail/<pk>/RoomDeleteView',views.RoomDeleteView.as_view(),name='RoomDeleteView'),
    path('JoinerRoomDetail/<pk>/RoomJoinersUpdateView',views.RoomJoinersUpdateView.as_view(),name='RoomJoinersUpdateView'),
    #path('JoinerRoomList/',views.JoinerRoomListView.as_view(),name='JoinerRoomList'),
    #path('JoinerRoomDetail/<int:pk>/',views.JoinerRoomDetailView,name='JoinerRoomDetail'),


]
