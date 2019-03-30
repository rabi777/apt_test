from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from rest_framework.response import Response
from rest_framework.views import APIView


class DataListApiView(APIView):
    def get(self, request):
        data = ['a', 'b', 'c', 'd', 'e', 'f']
        return Response(data)


class DataListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'api/data_list.html')
