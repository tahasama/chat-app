from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='User') #basename so that get_queryset work
router.register(r'room', views.PublicChatRoomViewSet)
#router.register(r'message', views.PublicChatRoomMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]