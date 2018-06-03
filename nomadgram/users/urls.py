from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(
        regex=r'^explore/$',
        view=views.ExploreUser.as_view(),
        name='explore_users'
    ),
    url(
        regex=r'^(?P<user_id>\w+)/follow/$',
        view=views.FollowUser.as_view(),
        name='follow_user'
    ),
    url(
        regex=r'^(?P<user_id>\w+)/unfollow/$',
        view=views.UnFollowUser.as_view(),
        name='unfollow_user'
    ),
   
   
]