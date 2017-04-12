from django.conf.urls import url
from . import views


urlpatterns = [
    # 第一条URL模式没有带入任何参数，它映射到post_list视图（view）。
    url(r'^$', views.post_list, name='post_list'),
    #第二条URL模式带上了以下4个参数映射到post_detail视图（view）中。
    #url(r'^$', views.PostListView.as_view(),name='post_list'),
    #添加一个新的URL模式来对应PostlistView类视图
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    #添加新的url对应视图中的post_share,url构建机制：主url开头，post_id对应的帖子ID/share.
    url(r'^(?P<post_id>\d+)/share/$', views.post_share,
    name='post_share'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$',views.post_list,
    name='post_list_by_tag'),
]