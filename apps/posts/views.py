
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.posts.models import Post
from apps.posts.serializer import PostSerializer
from apps.posts.permission import PostPermission


# Create your views here.

class PostAPIViewSet(GenericViewSet, mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )
    
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)

    def get_permissions(self):
        if self.action in ('list', ):
            return (AllowAny(), )
        if self.action in ('create', ):
            return (IsAuthenticated(), )
        if self.action in ('update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), PostPermission() )
        return (AllowAny(), )

