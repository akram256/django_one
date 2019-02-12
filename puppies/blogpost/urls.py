from django.conf.urls import url
from blogpost import views 


urlpatterns =[
   url (r'^api/v1/blogpost/(?P<pk>[0-9]+)$', views.get_delete_update_puppy, name='get_delete_update_puppy'),
   url(r'^api/v1/blogpost/$', views.get_post_puppies, name='get_post_puppy'),
]