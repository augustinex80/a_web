from django.conf.urls import url
from .views import PostList, PostDetail, TagList


urlpatterns = [
    url(r'^$', PostList.as_view(), name='list'),
    url(r'^category/(?P<cate_id>\d+)/(?P<cate_name>[^/]+)/$', PostList.as_view(), name='list_of_category'),
    url(r'^(?P<pid>\d+)/(?P<slug>[^/]+)/$', PostDetail.as_view(), name='detail'),
    url(r'^p/(?P<tid>\d+)/(?P<tname>[^/]+)/$', PostList.as_view(), name='tag_posts'),
    url(r'^all/$', TagList.as_view(), name='tags_list'),
]
