from django.conf.urls import url
from blogpost import views 


urlpatterns =[
   url (r'^api/v1/blogpost/(?P<pk>[0-9]+)$', views.get_delete_update_puppy, name='get_delete_update_puppy'),
   url(r'^api/v1/blogpost/$', views.get_post_puppies, name='get_post_puppy'),
   url(r'^api_auth/v1/users/$',views.create_user,name='create_user'),
   url(r'^api_auth/v1/login/$',views.login_user,name='login_user'),
]