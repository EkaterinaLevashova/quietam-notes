from django.urls import path, re_path
from qnote_app import views
from qnote_app.views import *

app_name = 'qnote_app'

urlpatterns = [
    path('', UserListView.as_view(), name='list'),
    re_path(r'^(?P<pk>[-\w]+)/$', views.UserDetailView.as_view(), name='detail')
]
