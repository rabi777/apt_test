from django.contrib import admin
from django.urls import path, include

from api.views import DataListView, DataListApiView

urlpatterns = [
    path('list/', DataListView.as_view(), name='list_view'),
    path('api/list/', DataListApiView.as_view(), name='api_data_view')
]
