from rest_framework import routers

from api.views import CommentViewSet, GroupViewSet, PostViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('v1/posts', PostViewSet, basename='posts')
router_v1.register('v1/groups', GroupViewSet, basename='groups')
router_v1.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
