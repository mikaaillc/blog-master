from django.urls import path
from .views import *
app_name='post'

urlpatterns = [

    path(r'index/',post_index,name='index'),
    path(r'create/',post_create,name='create'),

    path(r'<slug>/detail/',post_detail,name='detail'),
    path(r'<slug>/update/',post_update,name='update'),
    path(r'<slug>/delete/',post_delete,name='delete'),

]