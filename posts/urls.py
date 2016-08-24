from django.conf.urls import url
from .views import PostList, PostDetail


urlpatterns = [
    url(r'^index.html$', PostList.as_view(), name='list'),
    url(r'^category/(?P<cate_id>\d+)/$', PostList.as_view(), name='list_of_category'),
    url(r'^(?P<pid>\d+)/(?P<slug>[^/]+)/$', PostDetail.as_view(), name='detail'),
    url(r'^t/(?P<tid>\d+)/(?P<tname>[^/]+)/$', PostList.as_view(), name='tag_posts'),
]
